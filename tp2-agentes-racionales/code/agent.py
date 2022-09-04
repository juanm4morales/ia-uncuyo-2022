from enviroment import Enviroment

class Agent:
    def __init__(self,enviroment:Enviroment):
        self.enviroment=enviroment
    
    def up(self):
        self.enviroment.accept_action((0,1), False)
    
    def down(self):
        self.enviroment.accept_action((0,-1), False)
        
    def left(self):
        self.enviroment.accept_action((-1,0), False)
    
    def right(self):
        self.enviroment.accept_action((1,0), False)
    
    def suck(self):
        self.enviroment.accept_action((0,0), True)
    
    def idle(self):
        self.enviroment.accept_action((0,0), False)
        
    def perspective(self):
        agentPosition=self.enviroment.agentPosition
        dirtyCell=self.enviroment.is_dirty()
        return (dirtyCell,agentPosition)
    
    #def think(self):
        