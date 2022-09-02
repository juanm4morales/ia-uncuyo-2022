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
        grid = make_grid(sizeX,sizeY)
        self.grid = dirty_grid(grid, dirty_cells)
        self.agentPosition=None
                
    def make_grid(sizeX,sizeY):
        grid=[]
        for i in range(sizeX):
            grid.append([])
            for j in range(sizeY):
                cell=Cell()                
                grid[i].append(cell)
            
        return grid
    
    def dirty_grid(grid, dirty_cells):
        sizeX=len(grid)
        sizeY=len(grid[0])
        while (dirty_cells>0):
            x=random.randint(0, sizeX)
            y=random.randint(0, sizeY)
            if (grid[x][y]!='d'):
                grid[x][y]='d'
                dirty_cells=dirty_cells-1

    def update_agent():
        return -1

        
            
                