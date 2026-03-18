import random
from dnn_model import DNNModel
from memory_model import FeRAMMemory
from wear_leveling import wear_level
from dual_mode import configure_modes

class Simulator:

    def __init__(self):

        self.memory = FeRAMMemory(
            num_blocks=1024,
            endurance_limit=10**6
        )

        configure_modes(self.memory)    # randomly assign volatile mode

    def run_training(self, model_name):

        print("Start Training run")
        # model = DNNModel(model_name)
        model = DNNModel()

        trainings = 0

        while not self.memory.is_failed():

            accesses = model.generate_access_pattern()  # generate random write count for each layer

            for writes in accesses:

                for _ in range(writes):

                    block = random.randint(0, 1023) # Pick a random block

                    self.memory.write(block)

            wear_level(self.memory)

            trainings += 1
            if trainings == 2 :
                break

        return trainings