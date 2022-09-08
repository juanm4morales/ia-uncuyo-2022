import random
import math
class Cell:
    def __init__(self):
        self.dirty=False
        self.agent=False
       
class Enviroment:
    def __init__(self,sizeX,sizeY,init_posX,init_posY,dirt_rate):
        self.sizeX=sizeX
        self.sizeY=sizeY
        self.init_posX=init_posX
        self.init_posY=init_posY
        self.currentPosX=init_posX
        self.currentPosY=init_posY
        self.dirt_rate=dirt_rate
        self.amountOfDirt=math.ceil(dirt_rate*sizeX*sizeY)
        self.grid: list[list[Cell]] = self.make_grid(sizeX, sizeY)
        self.dirty_grid()
        self.grid[init_posY][init_posX].agent=True
        self.agentPosition=[init_posX,init_posY]
        self.cellsCleaned=0

               
    def make_grid(self,sizeX,sizeY):
        grid=[]
        for i in range(0,sizeY):
            grid.append([])
            for j in range(0,sizeX):
                cell=Cell()                
                grid[i].append(cell)
        return grid
   
    def dirty_grid(self):
        sizeX=len(self.grid)
        sizeY=len(self.grid[0])
        remainingDirt=self.amountOfDirt
        while (remainingDirt>0):
            x=random.randint(0, sizeX-1)
            y=random.randint(0, sizeY-1)
            if not(self.grid[y][x].dirty):
                self.grid[y][x].dirty=True
                remainingDirt=remainingDirt-1
 
    def print_enviroment(self):
        grid = self.grid
        for i in range (0,self.sizeX):
            print("|",end="")
           
            gridRow=grid[i]
           
            for j in range(0,self.sizeY):
                gridCell=gridRow[j]
                if gridCell.dirty:
                    print("{",end="")
                    if gridCell.agent:
                        print("A",end="")
                    else:
                        print(" ",end="")
                    print("}|",end="")
                else:
                    if gridCell.agent:
                        print(" A |",end="")
                    else:
                        print("   |",end="")
            print("")
        print("")
                       
    
    def accept_action(self,movement: (int,int),suck:bool):
        if not(suck) and abs(movement[0]+movement[1])==1:
            newX = movement[0] + self.agentPosition[0]
            newY = movement[1] + self.agentPosition[1]
            if (newX>=0 and newX<self.sizeX) and (newY>=0 and newY<self.sizeY):
                self.move_agent(newX, newY)
                return 0
            else:
                return -1
        else:
            if (self.grid[self.agentPosition[1]][self.agentPosition[0]].dirty)==True:
                self.grid[self.agentPosition[1]][self.agentPosition[0]].dirty=False
                self.cellsCleaned+=1
            return 0
                
    def move_agent(self,x,y):
        self.grid[self.agentPosition[1]][self.agentPosition[0]].agent=False
        self.agentPosition[0]=x
        self.agentPosition[1]=y
        #print("x= " +str(x))
        #print("y= " +str(y))
        self.grid[y][x].agent=True
        
    def is_dirty(self):
        return self.grid[self.agentPosition[1]][self.agentPosition[0]].dirty
    
    
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