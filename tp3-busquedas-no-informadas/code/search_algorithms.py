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

                if nextPosition not in explored and not(inFrontier(nextPosition, frontier)):
                    if nextPosition==last_pos:
                        return child
                    frontier.insert(0, child)
    return None

def inFrontier(position, frontier:list[Node]):
    for i in range(0,len(frontier)):
        if frontier[i].position==position:
            return True
    return False
    

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

                if nextPosition not in explored and not(inFrontierC(nextPosition, frontier)):
                    if nextPosition==last_pos:
                        return child
                    frontier.insert(0, (0,child))
    return None

def inFrontierC(position, frontier:list[(int,Node)]):
    for i in range(0,len(frontier)):
        if frontier[i][1].position==position:
            return True
    return False

def dfs(grid:list[list[enviroment.Cell]],init_pos:tuple,last_pos:tuple,explored:set):
    node = Node(init_pos)
    if init_pos==last_pos:
        return node
    actions=[(0,1),(0,-1),(-1,0),(1,0)]
    frontier=[node]

    while True:
        if len(frontier)==0:
            return None
        node = frontier.pop(0)
        explored.add(node.position)
        for action in actions:
            if is_valid(grid,node.position,action):
                nextPosition=tuple(map(operator.add,node.position, action))
                child = Node(nextPosition,0, node)
                if nextPosition not in explored and not(inFrontier(nextPosition, frontier)):
                    if nextPosition==last_pos:
                        return child
                    frontier.insert(0, child)


def dls(grid:list[list[enviroment.Cell]],init_pos:tuple,last_pos:tuple,explored:set,limit:int):
    node = Node(init_pos)
    if init_pos==last_pos:
        return node
    actions=[(0,1),(0,-1),(-1,0),(1,0)]
    frontier=[node]

    while True:
        if len(frontier)==0:
            return None
        node = frontier.pop(0)
        explored.add(node.position)
        limit=limit-1
        if limit<=0:
            # print("cutoff")
            return None
        for action in actions:
            if is_valid(grid,node.position,action):
                nextPosition=tuple(map(operator.add,node.position, action))
                child = Node(nextPosition,0, node)

                if nextPosition not in explored and not(inFrontier(nextPosition, frontier)):
                    if nextPosition==last_pos:
                        return child
                    frontier.insert(0, child)


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
    