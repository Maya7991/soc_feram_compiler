from simulator import Simulator
import plots

sim = Simulator()   # initializes FeRAM memory

result = sim.run_training("ResNet20")   # runs training until memory fails (endurance limit)

print("Memory survived trainings:", result)

# plot memory wear distribution
plots.plot_wear(sim.memory)
plots.plot_top_blocks(sim.memory)