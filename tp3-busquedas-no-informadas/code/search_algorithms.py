import operator
import enviroment
import queue
import random

class Node:
    def __init__(self,position:(int,int),cost=0,parent=None):
        self.parent:Node=parent
        self.position=position
        self.cost=cost

def bfs(grid:list[list[enviroment.Cell]],init_pos:tuple,last_pos:tuple,explored:set):
    
    node = Node(init_pos)
    if init_pos==last_pos:
        return node
    actions=[(0,1),(0,-1),(-1,0),(1,0)]
    frontier=[node]

    while True:
        if len(frontier)==0:
            return None
        node = frontier.pop()
        explored.add(node.position)
        for action in actions:
            if is_valid(grid,node.position,action):
                nextPosition=tuple(map(operator.add,node.position, action))
                child = Node(nextPosition,0, node)

                if nextPosition not in explored and nextPosition not in frontier:
                    if nextPosition==last_pos:
                        return child
                    frontier.insert(0, child)

def ucs(grid:list[list[enviroment.Cell]],init_pos:tuple,last_pos:tuple,explored:set):
    node = Node(init_pos,0)
    if init_pos==last_pos:
        return node
    actions=[(0,1),(0,-1),(-1,0),(1,0)]
    frontier:list[(int,Node)]=[(node.cost,node)]

    while True:
        if len(frontier)==0:
            return None
    
        tupNode:list[(int,Node)] = frontier.pop()
        node = tupNode.__getitem__(1)
        explored.add(node.position)
        for action in actions:
            if is_valid(grid,node.position,action):
                nextPosition=tuple(map(operator.add,node.position, action))
                cost=grid[nextPosition[0]][nextPosition[1]].cost
                child = Node(nextPosition, cost,node)

                if nextPosition not in explored and (cost,nextPosition) not in frontier:
                    if nextPosition==last_pos:
                        return child
                    frontier.insert(0, (0,child))

def dls(grid:list[list[enviroment.Cell]],init_pos:tuple,last_pos:tuple,limit:int,explored:set):
    actions=[(0,1),(0,-1),(-1,0),(1,0)]
    return (recursive_dls(grid, actions, Node(init_pos),last_pos,limit,explored))

def recursive_dls(grid:list[list[enviroment.Cell]], actions:list[(int,int)], node:Node, last_pos:tuple, limit:int,explored:set):
    #print(node.position)
    explored.add(node.position)
    if node.position==last_pos:
        return node
    elif limit==0:

        return 0
    else:
        cutoff_occurred=False

        for action in actions:
            if is_valid(grid, node.position, action):
                nextPosition=tuple(map(operator.add,node.position, action))
                child=Node(nextPosition, 0, node)
                if nextPosition not in explored:
                    result = recursive_dls(grid, actions, child, last_pos, limit-1,explored)
                    if result == 0:
                        cutoff_occurred = True
                    elif result != -1:
                        return result
        if cutoff_occurred:
            return 0
        else:
            return -1

def dfs(grid:list[list[enviroment.Cell]],init_pos:tuple,last_pos:tuple,explored:set):
    actions=[(0,1),(0,-1),(-1,0),(1,0)]
    return (recursive_dfs(grid, actions, Node(init_pos),last_pos,explored))

def recursive_dfs(grid:list[list[enviroment.Cell]], actions:list[(int,int)], node:Node, last_pos:tuple ,explored:set):
    explored.add(node.position)
    if node.position==last_pos:
        return node

    for action in actions:
        if is_valid(grid, node.position, action):
            nextPosition=tuple(map(operator.add,node.position, action))
            child=Node(nextPosition, 0, node)
            if nextPosition not in explored:
                result = recursive_dfs(grid, actions, child, last_pos,explored)
                if result!=None:
                    return result

    return None

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
    