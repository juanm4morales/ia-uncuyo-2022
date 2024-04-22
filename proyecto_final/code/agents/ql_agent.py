

import numpy as np

class QLAgent:
    
    def __init__(self, enviroment, gamma, alpha, startEpsilon, endEpsilon, decayRate):
        self.enviroment = enviroment
        self.lastReward = 0
        self.accReward = 0
        self.action = None
        self.gamma = gamma
        self.alpha = alpha
        self.startEpsilon = startEpsilon
        self.endEpsilon = endEpsilon
        self.decayRate = decayRate
        
    def epsilonGreedyPolicy(self, qTable, state, epsilon):
        randint = random.uniform(0,1)
        if randint > epsilon:
            action = np.argmax(qTable[state])
        else:
            action = self.enviroment.actionSpace.sample()
    
    def train(self, episodes):
        for episode in range(episodes):
            epsilon = self.endEpsilon + (self.startEpsilon - self.endEpsilon) * np.exp(-decayRate*episode)
            enviroment.reset()
            step = 0
            done = False
            
            while (enviroment.finishedSimulation()):
                action = epsilonGreedyPolicy(qTable, state, epsilon)
                
                newState, reward, done, info = enviroment.step(action)
                qTable[state][action] = qTable[state][action] + learningRate * (reward + gamma * np.max(qTable[newState]) - qtable[state][action])
                
                if done:
                    break
                    
                state = newState
                                    
        return qTable
        