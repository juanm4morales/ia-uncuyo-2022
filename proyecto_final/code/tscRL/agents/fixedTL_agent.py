import numpy as np
import random

import sys
import os

class FixedTLAgent:
    """
        Q Learning agent with epsilon greedy policy
        
        Attributes:
            environment : SumoEnvironment
                The environment where agent acts in
            currentState : tuple
                Current state
    """
    
    def __init__(self, enviroment):
        enviroment.fixedTL = True
        self.enviroment = enviroment
        self.currentState = enviroment.getCurrentState()
        
    def run(self, episodes):
        metrics = []
        for episode in range(episodes):
            step = 0
            done = False
            while not done:
                newState, reward, done, info = self.enviroment.step()
                info["episode"] = episode
                metrics.append(info)
                if done:
                    break        
                self.currentState = newState
            self.enviroment.reset()
        self.enviroment.close()
        
        return metrics
        