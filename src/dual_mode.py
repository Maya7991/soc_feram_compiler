import random

def configure_modes(memory):

    for i in range(memory.num_blocks):

        # randomly assign volatile mode
        if random.random() < 0.3:
            memory.mode[i] = "volatile"
        else:
            memory.mode[i] = "nonvolatile"