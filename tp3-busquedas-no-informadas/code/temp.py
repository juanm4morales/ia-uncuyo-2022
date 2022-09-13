def dls(grid:list[list[enviroment.Cell]],init_pos:tuple,last_pos:tuple,limit:int,explored:set):
    actions=[(0,1),(0,-1),(-1,0),(1,0)]
    return (recursive_dls(grid, actions, Node(init_pos),last_pos,limit,explored))

def recursive_dls(grid:list[list[enviroment.Cell]], actions:list[(int,int)], node:Node, last_pos:tuple, limit:int,explored:set):

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
    result =  recursive_dfs(grid, actions, Node(init_pos),last_pos,explored)
    return result

def recursive_dfs(grid:list[list[enviroment.Cell]], actions:list[(int,int)], node:Node, last_pos:tuple ,explored:set):
    print(rec)
    rec=rec+1
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