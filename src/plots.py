import matplotlib.pyplot as plt


def plot_wear(memory):

    plt.hist(memory.write_count, bins=50)

    plt.title("FeRAM Memory Wear Distribution")
    plt.xlabel("Write Cycles per Block")
    plt.ylabel("Number of Blocks")

    plt.savefig("write_cycle.png")

def plot_top_blocks(memory):

    sorted_wear = sorted(memory.write_count, reverse=True)[:20]

    plt.plot(sorted_wear)

    plt.title("Top 20 Most Worn Memory Blocks")
    plt.xlabel("Block Rank")
    plt.ylabel("Write Cycles")

    plt.savefig("most_worn_blocks.png")