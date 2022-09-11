import agents
import enviroment
import random

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
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    agent2=agents.Agent(env,"ucs")
    exploreAmount2=len(agent2.exploredNodes)
    results.append(exploreAmount2)
    agent2.think()
    env.resetEnviroment()
    agent3=agents.Agent(env,"dfs")
    exploreAmount3=len(agent3.exploredNodes)
    results.append(exploreAmount3)
    agent3.think()
    env.resetEnviroment()
    agent4=agents.Agent(env,"dls")
    exploreAmount4=len(agent4.exploredNodes)
    results.append(exploreAmount4)
    agent4.think()
    
    return results
    
    
size=100
n=30
obstacle_rate=0.1
results=[]
for i in range(0,n):
    results[i]=simulation(size, obstacle_rate)