from enviroment import Enviroment

class Agent:
    def __init__(self,enviroment:Enviroment):
        self.enviroment=enviroment
    
    def up(self):
        self.enviroment.update_agent()