import random
 
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
        dirty_cells=dirt_rate*sizeX*sizeY
        self.grid: list[list[Cell]] = self.make_grid(sizeX, sizeY)
        self.dirty_grid(self.grid, dirty_cells)
        self.grid[init_posY][init_posX].agent=True
        self.agentPosition=[init_posX,init_posY]
               
    def make_grid(self,sizeX,sizeY):
        grid=[]
        for i in range(0,sizeY):
            grid.append([])
            for j in range(0,sizeX):
                cell=Cell()                
                grid[i].append(cell)
        return grid
   
    def dirty_grid(self, grid : list[list[Cell]], dirty_cells):
        sizeX=len(grid)
        sizeY=len(grid[0])
        while (dirty_cells>0):
            x=random.randint(0, sizeX-1)
            y=random.randint(0, sizeY-1)
            if not(grid[y][x].dirty):
                grid[y][x].dirty=True
                dirty_cells=dirty_cells-1
 
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
            self.grid[self.agentPosition[1]][self.agentPosition[0]].dirty=False
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
 
       
env = Enviroment(10, 10, 0, 0, 0.8)

env.printGrid()
print(env.is_dirty())
env.update_agent((1,0), False)
env.update_agent((0,0), True)
env.printGrid()
env.update_agent((1,0), False)
print(env.is_dirty())
env.update_agent((0,0), True)
env.printGrid()
env.update_agent((1,0), False)
print(env.is_dirty())
env.update_agent((0,0), True)
env.printGrid()
env.update_agent((1,0), False)
print(env.is_dirty())
env.update_agent((0,0), True)
env.printGrid()

