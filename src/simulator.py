import random
from dnn_model import DNNModel
from memory_model import FeRAMMemory
from wear_leveling import wear_level
from dual_mode import configure_modes
from utils import NUM_BLOCKS

class Simulator:

    def __init__(self):
        # 1 block size = 256 KB
        # 112 blocks   = 28MB SRAM
        self.memory = FeRAMMemory(
            num_blocks=NUM_BLOCKS,
            endurance_limit=10**12
        )
        configure_modes(self.memory)    # randomly assigning volatile mode

    def run_training(self, model_name):

        print("Start Training run")
        model = DNNModel(model_name)

        trainings = 0

        accesses = model.generate_access_pattern()
        print(accesses)

        while not self.memory.is_failed():
            for writes in accesses:
                writes = writes * 3 # training memory access ~ 3 x inference memory access
                block = random.randint(0, NUM_BLOCKS-1)
                self.memory.write_bulk(block, writes*100)   # 1 training is 100 epochs in the paper

            wear_level(self.memory)

            trainings += 1
            # if trainings > 1000:
            #     break

        return trainings