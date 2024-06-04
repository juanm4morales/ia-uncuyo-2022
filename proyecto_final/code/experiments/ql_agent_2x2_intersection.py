import sys
import os

current_dir=os.path.dirname(__file__)

sys.path.append(os.path.join(current_dir, '..'))
print(sys.path)


from tscRL.environments.environment import SumoEnvironment
from tscRL.agents.ql_agent import QLAgent

if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")
    

env = SumoEnvironment("nets/2x2_intersection/interseccion.sumocfg", 5, 2, 4, 60, gui=True, edges=False, discreteIntervals=6, laneInfo="halted", rewardFn="diff_halted")

agent = QLAgent(env, 0.99, 0.1, 0.05, 0.005, 1.0)

agent.train(1)

