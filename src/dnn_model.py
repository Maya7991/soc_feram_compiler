import torch
import torchvision.models as models

class DNNModel:

    def __init__(self):

        # load a real network
        self.model = models.resnet18()

    def generate_access_pattern(self):

        accesses = []

        for name, layer in self.model.named_modules():

            if isinstance(layer, torch.nn.Conv2d):

                weight_access = layer.weight.numel()
                activation_access = layer.out_channels * 32 * 32    # just checking -hardcoded for now

                total_writes = weight_access + activation_access

                accesses.append(total_writes)

            elif isinstance(layer, torch.nn.Linear):

                weight_access = layer.weight.numel()
                accesses.append(weight_access)

        return accesses

        
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