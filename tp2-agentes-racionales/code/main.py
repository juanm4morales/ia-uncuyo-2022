from enviroment import Enviroment
from agent import Agent
import random



def simulation(sizeX,sizeY,dirt_rate):
    init_posX=random.randint(0, sizeX-1)
    init_posY=random.randint(0, sizeY-1)
    enviroment=Enviroment(sizeX, sizeY, init_posX, init_posY, dirt_rate)
    agent=Agent(enviroment)
    enviroment.print_enviroment()
    print("")
    agent.think()
    enviroment.print_enviroment()
    


simulation(12, 12, 0.8)