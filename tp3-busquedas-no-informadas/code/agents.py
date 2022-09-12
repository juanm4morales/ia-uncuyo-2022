from enviroment import Enviroment
import search_algorithms as search
import string
import math
import copy

import sys

sys.setrecursionlimit(100000)
class Agent:
    def __init__(self,enviroment:Enviroment, strategy:str="bfs"):
        self.enviroment=enviroment
        self.agentPosition=self.enviroment.agentPosition
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
        print(self.findPath())
        """
        agentSequence:list[(int,int)]=self.findPath()
        if agentSequence==None:
            print("No solution")
            return False
        # print(agentSequence)
        self.startSequence(agentSequence)
        #self.enviroment.print_enviroment()
        return True
        """
    
    def findPath(self) -> list[(int,int)] :
        grid=self.enviroment.grid
        last_pos=(self.enviroment.endR,self.enviroment.endC)
        init_pos=(self.agentPosition[0],self.agentPosition[1])
        """
        solution:search.Node=None
        if self.strategy=="bfs":
            solution=search.bfs(grid, init_pos, last_pos, self.exploredNodes)
        elif self.strategy=="ucs":
            solution=search.ucs(grid, init_pos, last_pos, self.exploredNodes)
        elif self.strategy=="dfs":
        """
        print("!!!")
        solution=search.DFS(grid, init_pos, last_pos, self.exploredNodes)
        print("!!!")
        """
        elif self.strategy=="dls":
            limit = math.ceil(len(grid)*len(grid[0])/2)
            solution=search.dls(grid, init_pos, last_pos, limit, self.exploredNodes)
        else:
            print("?")
        """

        
        
        if type(solution) != search.Node:
            if solution==0:
                print("Cutoff occurred")
            elif solution==-1 or solution==None:
                print("Failure")
            return None
        else:
            path:list[(int,int)]=[]
            while solution!=None:
                path.insert(0, solution.position)
                solution=solution.parent
            return path
    def amountOfExploration(self):
        return(self.exploredNodes)
    
    

env=Enviroment(80, 80, 0, 0, 59, 78, 0.1)
env.print_enviroment()
agent=Agent(env,"dfs")
agent.think()
print(len(agent.exploredNodes))
print(sys.getrecursionlimit())
