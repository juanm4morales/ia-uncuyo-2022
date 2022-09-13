from enviroment import Enviroment
import search_algorithms as search
import string
import math
import copy

import sys


class Agent:
    def __init__(self,enviroment:Enviroment, strategy:str="bfs"):
        self.enviroment=enviroment
        self.agentPosition=copy.copy(self.enviroment.agentPosition)
        if strategy.lower() == "bfs":
            self.strategy="bfs"
        elif strategy.lower() == "ucs":
            self.strategy="ucs"
        elif strategy.lower() == "dfs":
            self.strategy="dfs"
        elif strategy.lower() == "dls":
            self.strategy="dls"
        else:
            print("?")
        self.exploredNodes:set=set()
            
    
    def up(self):
        return 0
    
    def down(self):
        return 0
        
    def left(self):
        return 0
    
    def right(self):
        return 0

    def startSequence(self, agentSequence:list[(int,int)]):
        for move in agentSequence:
            self.agentPosition[0]=move[0]
            self.agentPosition[1]=move[1]
            self.enviroment.update_agent(self.agentPosition)
            
    def think(self):
        agentSequence:list[(int,int)]=self.findPath()
        if agentSequence==None:
            # print("No solution")
            return False
        self.startSequence(agentSequence)
        #print(agentSequence)
        #self.enviroment.print_enviroment()
        return True

    
    def findPath(self) -> list[(int,int)] :
        grid=self.enviroment.grid
        last_pos=(self.enviroment.endR,self.enviroment.endC)
        init_pos=(self.agentPosition[0],self.agentPosition[1])

        solution:search.Node=None
        if self.strategy=="bfs":
            solution=search.bfs(grid, init_pos, last_pos, self.exploredNodes)
        elif self.strategy=="ucs":
            solution=search.ucs(grid, init_pos, last_pos, self.exploredNodes)
        elif self.strategy=="dfs":
            solution=search.dfs(grid, init_pos, last_pos, self.exploredNodes)
        elif self.strategy=="dls":
            limit = math.ceil(len(grid)*len(grid[0])/2)
            solution=search.dls(grid, init_pos, last_pos, self.exploredNodes, limit)
        else:
            print("?")
        
        if solution==None:
            return None
        else:
            path:list[(int,int)]=[]
            while solution!=None:
                path.insert(0, solution.position)
                solution=solution.parent
            return path
    def amountOfExploration(self):
        return(self.exploredNodes)
    
    


