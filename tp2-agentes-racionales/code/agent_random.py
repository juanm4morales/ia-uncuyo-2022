from enviroment import Enviroment
import random

class Agent:
    def __init__(self,enviroment:Enviroment):
        self.enviroment=enviroment
        self.initLifeTime=1000
        self.lifeTime=self.initLifeTime
    
    def up(self):
        self.lifeTime-=1
        if self.lifeTime<=0:
            return -2
        else:
            return self.enviroment.accept_action((0,1), False)
    
    def down(self):
        self.lifeTime-=1
        if self.lifeTime<=0:
            return -2
        else:
            return self.enviroment.accept_action((0,-1), False)
        
    def left(self):
        self.lifeTime-=1
        if self.lifeTime<=0:
            return -2
        else:
            return self.enviroment.accept_action((-1,0), False)
    
    def right(self):
        self.lifeTime-=1
        if self.lifeTime<=0:
            return -2
        else:
            return self.enviroment.accept_action((1,0), False)
    
    def suck(self):
        self.lifeTime-=1
        if self.lifeTime<=0:
            return -2
        else:
            return self.enviroment.accept_action((0,0), True)
    
    def idle(self):
        return self.enviroment.accept_action((0,0), False)
        
    def perspective(self):
        agentPosition=self.enviroment.agentPosition
        dirtyCell=self.enviroment.is_dirty()
        return (dirtyCell,agentPosition)
    
    def start(self):
        self.think()

    # Mediante el método think, el agente supone que se encuentra en una grilla rectangular y recorre esta mediante un barrido de extremo a extremo.
    def think(self):
        while self.lifeTime>0:
            action=random.randint(0, 5)
            if action==0:
                self.idle()
            elif action==1:
                self.left()
            elif action==2:
                self.right()
            elif action==3:
                self.up()
            elif action==4:
                self.down()
            elif action==5:
                self.suck()
            else:
                return None
                