import torch
import torch.nn as nn

from utils import MODEL_MAP

class DNNModel:

    def __init__(self, name):
        if name not in MODEL_MAP:
            raise ValueError(f"Unknown model: {name}")
        self.model = MODEL_MAP[name]()
        self.model.eval()

        # self.dummy_input = torch.randn(1, 3, 224, 224)

    # Calculate the memory access per inference
    def generate_access_pattern(self):

        accesses = []

        def hook_fn(module, input, output):

            if isinstance(module, nn.Conv2d):
                
                weight_access = module.weight.numel()   # weight accesses
                input_access = input[0].numel()         # input activations                
                output_access = output.numel()          # output activations
                total_writes = weight_access + input_access + output_access
                accesses.append(total_writes)

            elif isinstance(module, nn.Linear):
                # forgot to count input
                input_access = input[0].numel()
                weight_access = module.weight.numel()
                output_access = output.numel()
                accesses.append(weight_access + input_access + output_access)

        hooks = []

        for layer in self.model.modules():
            hooks.append(layer.register_forward_hook(hook_fn))

        # dummy input (ImageNet/CIFAR-10)
        x = torch.randn(1, 3, 224, 224)
        self.model(x)

        # remove hooks
        for h in hooks:
            h.remove()

        return accesses



    # def generate_access_pattern(self):

    #     accesses = []
    #     for name, layer in self.model.named_modules():

    #         if isinstance(layer, torch.nn.Conv2d):

    #             weight_access = layer.weight.numel()
    #             activation_access = layer.out_channels * 32 * 32    # just checking -hardcoded for now

    #             total_writes = weight_access + activation_access

    #             accesses.append(total_writes)

    #         elif isinstance(layer, torch.nn.Linear):

    #             weight_access = layer.weight.numel()
    #             accesses.append(weight_access)

    #     return accesses

        
# import random
# 
# class DNNModel:
    
#     def __init__(self, name):
#         self.name = name
        
#         if name == "ResNet20":
#             self.layers = 20
#         elif name == "ResNet18":
#             self.layers = 18
#         else:
#             self.layers = 10

#     def generate_access_pattern(self):
        
#         accesses = []
        
#         for l in range(self.layers):
#             writes = random.randint(1000, 5000)
#             accesses.append(writes)
            
#         return accesses