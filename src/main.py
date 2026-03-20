from simulator import Simulator
from utils import MODEL_MAP

import argparse
import plots


if __name__ == "__main__":

    # Parse command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("dnn_model",
                        type=str.lower,
                        choices = MODEL_MAP.keys(),
                        help = "Choose the DNN model")
    args = parser.parse_args()
    print(f"Selected model: {args.dnn_model}")


    # start simulator
    sim = Simulator()   # initializes FeRAM memory
    result = sim.run_training(args.dnn_model)   # runs training until memory fails (endurance limit)
    print("Memory survived trainings:", result)


    # plot memory wear distribution
    plots.plot_wear(sim.memory)
    plots.plot_top_blocks(sim.memory)