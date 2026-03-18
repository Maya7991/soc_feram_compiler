def wear_level(memory):

    most_used = max(range(memory.num_blocks),
                    key=lambda x: memory.write_count[x])

    least_used = min(range(memory.num_blocks),
                     key=lambda x: memory.write_count[x])

    # swap wear
    memory.write_count[most_used], memory.write_count[least_used] = \
        memory.write_count[least_used], memory.write_count[most_used]