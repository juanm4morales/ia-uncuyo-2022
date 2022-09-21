from typing import Tuple
import enviroment
import operator
import math

class Node:
    def __init__(self,position:Tuple[int,int],gCost=0,parent=None):
        self.parent:Node=parent
        self.position=position
        self.gCost=gCost


def astar(grid:list[list[enviroment.Cell]],init_pos:tuple,last_pos:tuple,explored:set):
    node:Node = Node(init_pos,0)
    if init_pos==last_pos:
        return node
    actions=[(0,1),(0,-1),(-1,0),(1,0)]
    frontier:list[(int,Node)]=[(0,node)]
    fCost = 0
    while True:
        if len(frontier)==0:
            return None
        
        tupNode:list[(int,Node)] = frontier.pop()
        
        node = tupNode.__getitem__(1)
        explored.add(node.position)
        for action in actions:
            if is_valid(grid,node.position,action):
                nextPosition=tuple(map(operator.add,node.position, action))
                gCost=grid[nextPosition[0]][nextPosition[1]].cost+node.gCost
                child = Node(nextPosition, gCost,node)


                hCost = math.sqrt(((last_pos[0]-nextPosition[0])*10)**2+((last_pos[1]-nextPosition[1])*10)**2)

                fCost = gCost + hCost
                if nextPosition not in explored and not(inFrontierC(nextPosition, frontier)):
                    if nextPosition==last_pos:
                        return child
                    frontier.insert(0, (fCost,child))
                    frontier.sort(key=lambda x: x[0],reverse=True)
                
    return None


def printFrontier(frontier):
    for i in range(0,len(frontier)):
        print(frontier[i][0], " - ",end="")
    print()
        
        

def inFrontierC(position, frontier:list[(int,Node)]):
    for i in range(0,len(frontier)):
        if frontier[i][1].position==position:
            return True
    return False

def is_valid(grid:list[list[enviroment.Cell]],position:tuple,action:tuple):  
    result=tuple(map(operator.add,position, action))
    rows=len(grid)
    cols=len(grid[position[1]])
    if result[0]<0 or result[0]>=rows:
        return False
    if result[1]<0 or result[1]>=cols:
        return False
    if grid[result[0]][result[1]].obstacle:
        return False
    return True