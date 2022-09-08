from enviroment import Enviroment
from agent import Agent
from agent_random import Agent as AgentRandom
import random
import csv

def simulation(sizeX,sizeY,dirt_rate):
    init_posX=random.randint(0, sizeX-1)
    init_posY=random.randint(0, sizeY-1)
    enviroment=Enviroment(sizeX, sizeY, init_posX, init_posY, dirt_rate)
    agent=AgentRandom(enviroment)
    #enviroment.print_enviroment()
    agent.start()
    return enviroment.get_performance(agent.initLifeTime)
    #enviroment.print_enviroment()
    
def initMatrix(rows,cols):
    matrix=[]
    for i in range(0,rows):
        matrix.append([])
        for j in range(0,cols):
            matrix[i].append(0)
    return matrix

def printDirtSize(matrix,rows,cols):
    print("                 Dim Size                       ")
    print("       2x2   4x4   8x8  16x16    32x32     64x64      128x128       ")
    for i in range(0,len(rows)):
        print(cols[i],end="      ")
        for j in range(0,len(cols)):
            print(matrix[i][j],end="   ")
        print("")
        
#         
dirt_list_test=[0.1,0.2,0.4,0.8]
dim_list_test=[2,4,8,16,32,64,128]
performanceBySize=[]
performanceByDirt=[]
sumPerformanceDirtSize=initMatrix(len(dirt_list_test), len(dim_list_test))
dataset=[]
dataset.append(['Size','Dirt Ratio','Performance'])
n=10



for i in range(0,n): 
    for j in range(0,len(dirt_list_test)):
        performanceByDirt.append([])
        
        for k in range(0,len(dim_list_test)):
            performanceBySize.append([])
            performance=simulation(dim_list_test[k], dim_list_test[k], dirt_list_test[j])
            #print(performance)
            
            dataset.append([str(dim_list_test[k])+'x'+str(dim_list_test[k]), dirt_list_test[j], str(round(performance, 6))])
            
            performanceBySize[k].append(performance)
            performanceByDirt[j].append(performance)
            sumPerformanceDirtSize[j][k]+=performance



csvfile = open('dataset_sim_agent_rdm.csv','a',newline='')
writer=csv.writer(csvfile)
writer.writerows(dataset)
avgPerformanceDirtSize=[]
for i in range(0,len(dirt_list_test)):
    avgPerformanceDirtSize.append([])
    for j in range(0,len(dim_list_test)):
        avgPerformanceDirtSize[i].append(round(sumPerformanceDirtSize[i][j]/n,6))

printDirtSize(avgPerformanceDirtSize, dirt_list_test, dim_list_test)
