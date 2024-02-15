
class QLAgent:
    
    def __init__(self, enviroment, gamma, alpha):
        self.enviroment = enviroment
        self.lastReward = 0
        self.accReward = 0
        self.action = None
        self.gamma = gamma
        self.alpha = alpha
        # self.qTable