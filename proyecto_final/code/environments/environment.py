import sys
import os
current_dir=os.path.dirname(__file__)
parent_dir=os.path.dirname(current_dir)
sys.path.append(os.path.join(current_dir, '..'))
import traci
from sumolib import checkBinary
from typing import Dict
from util.discrete import Discrete

import random

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

class Vehicle:
    def __init__(self, position, length, maxSpeed):
        self.position = position
        self.length = length
        self.maxSpeed = maxSpeed
        self.waitingTime = 0
    
    def update(self, deltaTime):
        self.waitingTime += deltaTime
        
class Lane:
    def __init__(self, laneId, laneLength):
        # self.vehicleMinGap = vehicleMinGap
        # self.vehicles = []
        self.laneId = laneId
        # self.laneLength = laneLength
        self.lastStepHaltedVehicles = 0
        self.waitingTime = 0
        
    def update(self):
        self.lastStepHaltedVehicles = traci.edge.getLastStepHaltingNumber(self.laneId)
        self.waitingTime = traci.edge.getWaitingTime(self.laneId)
        
    """
    # Para gestionar vehículo por vehículo
    def removeVehicle(self, amount=1):
        for i in range(amount):
            vehicleRef = self.vehicles.pop(0)
            del vehicleRef # Elimino la referencia, así el garbage collector de python lo elimina de memoria
        
    def getTotalWaitingTime(self):
        return sum(vehicle.waitingTime for vehicle in self.vehicles)
    
    def getAvgWaitingTime(self):
        return self.getTotalWaitingTime() / len(self.vehicles)
    
    def getQueueLength(self):
        queueLength = 0
        for vehicle in self.vehicles:
            queueLength += (vehicle.length + self.vehicleMinGap)
        return queueLength
    
    
    def searchVehiclesByWaitingTime(self, maxTime):
        vehicleIds = traci.lane.getLastStepVehicleIDs(self.laneId)
        vehiclesLongWait = []
        vehicleWaitingTime = 0
        for vehicleId in vehicleIds:
            vehicleWaitingTime = traci.vehicle.getWaitingTime(vehicleId)
            if vehicleWaitingTime > maxTime:
                vehiclesLongWait.append((vehicleId, vehicleWaitingTime))
        
        return vehiclesLongWait
    """          
                    
class TrafficLight:
    class Phase:
        def __init__(self, state, yellowTransition):
            self.state = state
            self.yellowTransition = yellowTransition
            
    # n=north, s=south, e=east, w=weast, l=left turn allowed (without priority)
    # G=Green with priority, g=green without priority, y=yellow, r=red
    PHASES = {'init':       Phase("rrrrrrrrrrrrrrrr", "rrrrrrrrrrrrrrrr"),
              'ns_sn_l':    Phase("GGGgrrrrGGGgrrrr", "yyyyrrrryyyyrrrr"),
              'ew_we_l':    Phase("rrrrGGGgrrrrGGGg", "rrrryyyyrrrryyyy"),
              'sn':         Phase("rrrrrrrrGGGGrrrr", "rrrrrrrryyyyrrrr"),
              'ns':         Phase("GGGGrrrrrrrrrrrr", "yyyyrrrrrrrrrrrr"),
              'we':         Phase("rrrrrrrrrrrrGGGG", "rrrrrrrrrrrryyyy"),
              'ew':         Phase("rrrrGGGGrrrrrrrr", "rrrryyyyrrrrrrrr"),
              'ns_sn':      Phase("GGGrrrrrGGGrrrrr", "yyyrrrrryyyrrrrr"),
              'ew_we':      Phase("rrrrGGGrrrrrGGGr", "rrrryyyrrrrryyyr"),
              # 'ne_sw':    Phase("rrrGrrrrrrrGrrrr", "rrryrrrrrrryrrrr"),
              # 'wn_es':    Phase("rrrrrrrGrrrrrrrG", "rrrrrrryrrrrrrry")
              }
    
    def __init__(self, id, initialPhase, yellowTime, minGreenTime, maxGreenTime):
        self.id = id
        self.currentPhase = "init"
        self.nextPhase = initialPhase
        self.yellowTime = yellowTime
        self.minGreenTime = minGreenTime
        self.maxGreenTime = maxGreenTime

        self.yellow = False
        self.currentPhaseTime = 0
        
    def update(self):
        if (self.currentPhase != self.nextPhase):
            if (self.yellow and self.currentPhaseTime >= self.yellowTime) or not self.yellow:
                nextPhaseState = self.PHASES[self.nextPhase].state
                traci.trafficlight.setRedYellowGreenState(0, nextPhaseState)
                self.currentPhase = self.nextPhase
                self.currentPhaseTime = 0
                self.yellow = False
                
        traci.simulationStep() 
        self.currentPhaseTime += 1
    
    def canChange(self):
        return (
            not(self.yellow)
            and (self.currentPhaseTime >= self.minGreenTime)
            and (self.currentPhaseTime>=self.yellowTime)
            )
    
    def changePhase(self, newPhase):
        if (self.currentPhase != newPhase):
            if self.canChange() or (self.currentPhase == "init"):
                if (self.currentPhase != "init"):  
                    yellowPhaseState = self.PHASES[self.currentPhase].yellowTransition
                    traci.trafficlight.setRedYellowGreenState(0, yellowPhaseState)
                    self.yellow = True
                    
                previousPhaseTime = self.currentPhaseTime
                self.currentPhaseTime = 0
                self.nextPhase = newPhase
                    
                return previousPhaseTime
            else:
                # No ha pasado el mínimo de tiempo de duración de la fase
                return -1
        else:
            # La fase actual es la misma que la nueva
            return -2

class State:
    def __init__(self, tlPhase, lanes: Dict[str, Lane], discreteClass):
        self.discreteClass = discreteClass
        self.tlPhase = tlPhase
        self.discreteLaneQueue = self.discretizeLaneInfo(lanes)
        
    def getTupleState(self):
        return (self.tlPhase, *self.discreteLaneQueue)
    
    def discretizeLaneInfo(self, lanes: Dict[str, Lane]):
        # discreteLaneQueue: Dict[str, int] = {}
        discreteLaneQueue = []
        for lane in lanes.values():
            discreteLaneQueue.append(self.discreteClass.log_interval(lane.lastStepHaltedVehicles))
        return discreteLaneQueue
        
class SumoEnvironment:
    INTERSECTION_SIZE=4
    
    def __init__(self, sumocfgFile, deltaTime=3, yellowTime=2, minGreenTime=5, maxGreenTime=60, gui=False):
        self.sumocfgFile = sumocfgFile
        self.gui = gui
        
        if gui:
            self.sumoBinary = checkBinary("sumo-gui")
        else:
            self.sumoBinary = checkBinary("sumo")
            
        self.initializeSimulation()
        self.deltaTime = deltaTime
        tls_ids = traci.trafficlight.getIDList()
        
        assert(yellowTime < deltaTime)
        self.trafficLight = TrafficLight(tls_ids[0], "init", yellowTime, minGreenTime, maxGreenTime)
        self.previousStepHaltedVehicles = 0
                
        lanesIds = traci.trafficlight.getControlledLanes(tls_ids[0])

        # self.lanes = {} # Usar carriles
        self.edges: Dict[str, Lane] = {} # Usar aristas
        for laneId in lanesIds:
            if "in" in laneId:
                # Carril de entrada
                edgeId = traci.lane.getEdgeID(laneId)                     # aristas
                if edgeId not in self.edges:                              # aristas
                    self.edges[edgeId] = Lane(edgeId, traci.lane.getLength(laneId)) # aristas
                # self.lanes[lane] = Lane(traci.lane.getLength(lane))     # carriles   

        self.discreteClass = Discrete(6, 32)

    @property
    def actionSpace(self):
        return [actionKey for actionKey in self.trafficLight.PHASES if actionKey != 'init']
       
    def initializeSimulation(self):
        sumoCMD = [self.sumoBinary, "-c", self.sumocfgFile,
                   #"--tripinfo-output", "tripinfo.xml"
                   ]
        if self.gui:
            sumoCMD.append("-S")
        traci.start(sumoCMD)
          
    def getCurrentState(self):
        state = State(self.trafficLight.currentPhase, self.edges, self.discreteClass)
        return state.getTupleState()
    
    def getTotalHaltedVehicles(self):
        return sum(edge.lastStepHaltedVehicles for edge in self.edges.values())
        
    
    def computeReward(self):
        currentStepHaltedVehicles = self.getTotalHaltedVehicles()
        reward = self.previousStepHaltedVehicles-currentStepHaltedVehicles
        self.previousStepHaltedVehicles = currentStepHaltedVehicles
        return reward

    # Deprecated 
    def validAction(self, action):
        currentPhaseTime = self.trafficLight.currentPhaseTime
        return ((currentPhaseTime>self.trafficLight.minGreenTime 
                and currentPhaseTime>=self.trafficLight.yellowTime)
                or (traci.simulation.getTime()==0))
    
    def step(self, action):
        # previousPhaseTime = 0
        # TOMAR ACCIÓN
        self.trafficLight.changePhase(action)
        # PASO DE TIEMPO (deltaTime)   
        for _ in range(self.deltaTime):
            self.trafficLight.update()
        
        for edge in self.edges.values():
            edge.update()
        
        state = self.getCurrentState()
        # print(state)
        # print(action)
        reward = self.computeReward()
        done = traci.simulation.getMinExpectedNumber() == 0
        return state, reward, done
        
    def reset(self):
        
        traci.load(['-c', self.sumocfgFile])
        self.trafficLight.yellow = False
        self.trafficLight.currentPhase = "init"
        self.trafficLight.nextPhase = "init"
        self.trafficLight.currentPhaseTime = 0

        self.previousStepHaltedVehicles = 0
        
        for edgeKey in self.edges:
            self.edges[edgeKey].lastStepHaltedVehicles = 0
            self.edges[edgeKey].waitingTime = 0
            
        
'''
env = SumoEnvironment("nets/2x2_intersection/interseccion.sumocfg", 5, 2, 4, 60, gui=True)

print(env.trafficLight.PHASES.keys())
print(env.trafficLight.PHASES.keys())
print(env.trafficLight.PHASES.keys())

while (True):
    action = random.choice(list(env.trafficLight.PHASES.keys()))
    state, reward, done = env.step(action)
''' 