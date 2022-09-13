import agents
import enviroment
import random
import sys

import resultsPersistence as persistence

sys.setrecursionlimit(100000)
def simulation(results, size, obstacle_rate):
    initR = random.randint(0, size-1)
    initC = random.randint(0, size-1)
    endR = random.randint(0, size-1)
    endC = random.randint(0, size-1)
    
    while initR==endR and initC==endC:
        endR = random.randint(0, size-1)
        endC = random.randint(0, size-1)

    
    env=enviroment.Enviroment(size, size, initR, initC, endR, endC, obstacle_rate)
    
    agent1=agents.Agent(env,"bfs")
    agent1.think()
    exploreAmount1=len(agent1.exploredNodes)
    results.append(['bfs',str(exploreAmount1)])
    env.resetEnviroment()
    #print(exploreAmount1,end="  ")
    
    agent2=agents.Agent(env,"ucs")
    agent2.think()
    exploreAmount2=len(agent2.exploredNodes)
    results.append(['ucs',str(exploreAmount2)])
    env.resetEnviroment()
    #print(exploreAmount2,end="  ")
    
    agent3=agents.Agent(env,"dfs")
    agent3.think()
    exploreAmount3=len(agent3.exploredNodes)
    results.append(['dfs',str(exploreAmount3)])
    env.resetEnviroment()
    #print(exploreAmount3,end="  ")
    
    agent4=agents.Agent(env,"dls")
    agent4.think()
    exploreAmount4=len(agent4.exploredNodes)
    results.append(['dls',str(exploreAmount4)])
    env.resetEnviroment()
    #print(exploreAmount4,end="  ")
    
    return results
 

size=100
n=30
obstacle_rate=0.1
results=[]
results.append(['Search_Strategy','Explored_Nodes'])
for i in range(0,n):
    simulation(results ,size, obstacle_rate)
    #print("")
print(results)
print("---------------------------")
persistence.storeResultsCSV(results)
print(persistence.loadResults())