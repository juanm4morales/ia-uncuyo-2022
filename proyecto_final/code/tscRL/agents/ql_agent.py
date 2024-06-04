import numpy as np
import random

import sys
import os

class QLAgent:
    """
        Q Learning agent with epsilon greedy policy
        
        Attributes:
            environment : SumoEnvironment
                The environment where agent acts in
            currentState : tuple
                Current state
            lastReward : float
                Last reward aquired
            gamma : float
                Discount rate
            alpha : float
                Learning rate
            startEpsilon : float
                Exploration probability at start
            endEpsilon : float
                Minimum exploration probability
            decayRate : float
                Exponential decay rate for exploration probability
    """
    
    def __init__(self, enviroment, gamma, alpha, startEpsilon=1, endEpsilon=0.001, decayRate=0.0002):
        self.enviroment = enviroment
        self.currentState = enviroment.getCurrentState()
        self.lastReward = 0
        # self.accReward = 0
        # self.action = None
        self.gamma = gamma
        self.alpha = alpha
        self.startEpsilon = startEpsilon
        self.endEpsilon = endEpsilon
        self.decayRate = decayRate
        
        self.qTable = {self.currentState: {action: 0 for action in self.enviroment.actionSpace}}
        
    def epsilonGreedyPolicy(self, state, epsilon):
        randint = random.uniform(0,1)
        if randint > epsilon:
            action = max(self.qTable[state].items(), key=lambda x: x[1])[0]
            # action = np.argmax(self.qTable[state])
        else:
            action = random.choice(self.enviroment.actionSpace)
        return action
    
    def train(self, episodes):
        for episode in range(episodes):
            # Epsilon value with exponential decay 
            epsilon = self.startEpsilon
            step = 0
            done = False
            while not done:
                action = self.epsilonGreedyPolicy(self.currentState, epsilon)
                newState, reward, done = self.enviroment.step(action)
                
                if newState not in self.qTable:
                    self.qTable[newState] = {action: 0 for action in self.enviroment.actionSpace}
            
                self.qTable[self.currentState][action] = self.qTable[self.currentState][action] + self.alpha * (reward + self.gamma * max(self.qTable[newState].values()) - self.qTable[self.currentState][action])
    
                if done:
                    break
                    
                self.currentState = newState
                epsilon = self.endEpsilon + (self.startEpsilon - self.endEpsilon) * np.exp(-self.decayRate*step)
               
            self.enviroment.reset()
        self.enviroment.close()
                                    
        return self.qTable
        