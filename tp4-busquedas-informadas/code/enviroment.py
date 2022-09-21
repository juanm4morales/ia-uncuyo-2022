import random
import math
class Cell:
    def __init__(self,cost=0):
        self.obstacle=False
        self.agent=False
        self.goal=False
        self.cost=cost

       
class Enviroment:
    def __init__(self,rows,cols,initR,initC,endR,endC,obstacle_rate):
        # dimensions
        if initR==endR and initC==endC:
            raise Exception("Initial position must be different to the goal position.")            
            
        self.rows=rows
        self.cols=cols
        
        self.initR=initR
        self.initC=initC
        
        self.endR=endR
        self.endC=endC
        
        self.agentPosition=[initR,initC]
        self.obstacle_rate=obstacle_rate
        self.grid: list[list[Cell]] = self.make_grid(rows, cols)
        self.grid[initR][initC].agent=True
        self.grid[endR][endC].goal=True
        
        self.putObstacles()


               
    def make_grid(self,rows,cols):
        grid=[]
        for r in range(0,rows):
            grid.append([])
            for c in range(0,cols):
                cell=Cell()
                cell.cost=10;            
                grid[r].append(cell)
        return grid
   
    def putObstacles(self):
        sizeR=self.rows
        sizeC=self.cols
        obstaclesToPut=math.ceil(sizeR*sizeC*self.obstacle_rate)
        while (obstaclesToPut>0):
            r=random.randint(0, sizeR-1)
            c=random.randint(0, sizeC-1)
            if not(self.grid[r][c].obstacle) and not(self.grid[r][c].agent) and not(self.grid[r][c].goal):
                self.grid[r][c].obstacle=True
                self.grid[r][c].cost=math.inf
                obstaclesToPut=obstaclesToPut-1
 
    def print_enviroment(self):
        grid = self.grid
        for r in range (0,self.rows):
            print("|",end="")
           
            gridRow=grid[r]
           
            for c in range(0,self.cols):
                gridCell=gridRow[c]
                if gridCell.obstacle:
                    print(" # |",end="")
                    
                else:
                    if gridCell.goal and gridCell.agent:
                        print("[A]|",end="")
                    elif gridCell.agent:
                        print(" A |",end="")
                    elif gridCell.goal:
                        print("[ ]|",end="")
                    else:
                        print("   |",end="")
            print("")
        print("")
                                       
    def update_agent(self,position:list[int]):
        self.grid[self.agentPosition[0]][self.agentPosition[1]].agent=False
        self.grid[position[0]][position[1]].agent=True
        self.agentPosition[0]=position[0]
        self.agentPosition[1]=position[1]
        #self.print_enviroment()
    
    def resetEnviroment(self):
        self.grid[self.agentPosition[0]][self.agentPosition[1]].agent=False
        self.agentPosition[0]=self.initR
        self.agentPosition[1]=self.initC
        self.grid[self.initR][self.initC].agent=True
    
    # Para medir el rendimiento, 80% del peso recae en la proporción de celdas limpiadas. Un 20% del rendimiento depende del tiempo consumido por el agente
    def get_performance(self,agentLifeTime):
        
        cleanness=self.cellsCleaned/self.amountOfDirt
        print("Cells cleanes"+str(self.cellsCleaned))
        print("Amount of dirt"+str(self.amountOfDirt))
        desired_actions=1000-self.sizeX*self.sizeY+self.amountOfDirt
        if desired_actions<=0:
            performance=cleanness*0.8+agentLifeTime/(self.sizeX*self.sizeY+self.amountOfDirt)*0.2
        else:
            performance=cleanness
        return performance
    