from enviroment import Enviroment
import random

class Agent:
    
    
    def __init__(self,enviroment:Enviroment):
        self.enviroment=enviroment
        self.lifeTime=1000
    
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
    
    def think(self):
        
        initialCorner=random.randint(0, 3)
        # 0: TopLeft - 1: TopRight - 2: BottomLeft - 3: BottomRight
        self.search_corner(initialCorner)
        done = False
        if initialCorner==0:
            while not(done):
                if self.cleanToRight()==-2:
                    return None
                mov=self.down()
                if mov<0:
                    if mov==-2:
                        return None
                    else:
                        done=True
                        sbreak
                if self.cleanToLeft()==-2:
                    return 
                mov=self.down()
                if mov<0:
                    if mov==-2:
                        return None
                    else:
                        done=True
                        break
            
        elif initialCorner==1:
            while not(done):
                if self.cleanToLeft()==-2:
                    return None
                mov=self.down()
                if mov<0:
                    if mov==-2:
                        return None
                    else:
                        done=True
                        sbreak
                if self.cleanToRight()==-2:
                    return 
                mov=self.down()
                if mov<0:
                    if mov==-2:
                        return None
                    else:
                        done=True
                        break
        
        elif initialCorner==2:
            while not(done):
                if self.cleanToRight()==-2:
                    return None
                mov=self.up()
                if mov<0:
                    if mov==-2:
                        return None
                    else:
                        done=True
                        sbreak
                if self.cleanToLeft()==-2:
                    return 
                mov=self.up()
                if mov<0:
                    if mov==-2:
                        return None
                    else:
                        done=True
                        break
            
        elif initialCorner==3:
            while not(done):
                if self.cleanToLeft()==-2:
                    return None
                mov=self.up()
                if mov<0:
                    if mov==-2:
                        return None
                    else:
                        done=True
                        sbreak
                if self.cleanToRight()==-2:
                    return 
                mov=self.up()
                if mov<0:
                    if mov==-2:
                        return None
                    else:
                        done=True
                        break
            
    def search_corner(self,corner):
        if corner==0:
            while self.lifeTime>0:
                if (self.left())<0:
                    break
            while self.lifeTime>0:
                if (self.up())<0:
                    break                    
                
        if corner==1:
            while self.lifeTime>0:
                if (self.right())<0:
                    break
            while self.lifeTime>0:
                if (self.up())<0:
                    break    
        if corner==2:
            while self.lifeTime>0:
                if (self.left())<0:
                    break
            while self.lifeTime>0:
                if (self.down())<0:
                    break    
            
        if corner==3:
            while self.lifeTime>0:
                if (self.right())<0:
                    break
            while self.lifeTime>0:
                if (self.down())<0:
                    break
                
    def cleanToRight(self):
        while self.lifeTime>0:
            if self.enviroment.is_dirty():
                if self.suck()==-2:
                    return -2
            mov=self.right()
            if mov<0:
                if mov==-2:
                    return -2
                else:
                    return 1
            
    def cleanToLeft(self):
        while self.lifeTime>0:
            if self.enviroment.is_dirty():
                if self.suck()==-2:
                    return -1
            mov=self.left()
            if mov<0:
                if mov==-2:
                    return -1
                else:
                    return 1