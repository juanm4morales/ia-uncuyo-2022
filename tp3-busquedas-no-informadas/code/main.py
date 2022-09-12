import agents
import enviroment
import random
import sys

sys.setrecursionlimit(100000)
def simulation(size, obstacle_rate):
    initR = random.randint(0, size-1)
    initC = random.randint(0, size-1)
    endR = random.randint(0, size-1)
    endC = random.randint(0, size-1)
    
    while initR==endR and initC==endC:
        endR = random.randint(0, size-1)
        endC = random.randint(0, size-1)

    results=[]
    
    env=enviroment.Enviroment(size, size, initR, initC, endR, endC, obstacle_rate)
    
    agent1=agents.Agent(env,"bfs")
    agent1.think()
    exploreAmount1=len(agent1.exploredNodes)
    results.append(exploreAmount1)
    env.resetEnviroment()
    print(exploreAmount1,end="  ")
    
    agent2=agents.Agent(env,"bfs")
    agent2.think()
    exploreAmount1=len(agent2.exploredNodes)
    results.append(exploreAmount1)
    env.resetEnviroment()
    print(exploreAmount1,end="  ")
    
    agent3=agents.Agent(env,"bfs")
    agent3.think()
    exploreAmount1=len(agent3.exploredNodes)
    results.append(exploreAmount1)
    env.resetEnviroment()
    print(exploreAmount1,end="  ")
    
    agent4=agents.Agent(env,"bfs")
    agent1.think()
    exploreAmount1=len(agent4.exploredNodes)
    results.append(exploreAmount1)
    env.resetEnviroment()
    print(exploreAmount1,end="  ")
    

    
    return results
 
env=enviroment.Enviroment(80, 80, 0, 0, 79, 68, 0.1)
#env.print_enviroment()
agent=agents.Agent(env,"dfs")
agent.think()
print(len(agent.exploredNodes))
print(sys.getrecursionlimit())
"""
size=100
n=30
obstacle_rate=0.1
results=[]
for i in range(0,n):
    print("!")
    results.append(simulation(size, obstacle_rate))
    print("")
"""
#print(results)