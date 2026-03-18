class FeRAMMemory:
    def __init__(self, num_blocks, endurance_limit):
        self.num_blocks = num_blocks
        self.endurance_limit = endurance_limit
        
        # write counters
        self.write_count = [0] * num_blocks
        
        # mode: nonvolatile or volatile
        self.mode = ["nonvolatile"] * num_blocks

    def write(self, block_id):
        if self.mode[block_id] == "nonvolatile":
            self.write_count[block_id] += 1

    def is_failed(self):
        for w in self.write_count:
            if w >= self.endurance_limit:
                return True
        return False