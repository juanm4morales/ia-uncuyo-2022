import traci
from sumolib import checkBinary
from typing import Dict
from util.discrete import discrete

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
        self.lastStepHaltedVehicles = traci.lane.getLastStepHaltingNumber(self.laneId)
        self.waitingTime = traci.lane.getWaitingTime(self.laneId)
        
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
        self.currentPhase = self.PHASES[initialPhase]
        self.nextPhase = initialPhase
        self.yellowTime = yellowTime
        self.minGreenTime = minGreenTime
        self.maxGreenTime = maxGreenTime

        self.yellow = False
        self.currentPhaseTime = 0
        
    def update(self):
        if (self.currentPhase != self.nextPhase):
            if (self.yellow and self.currentPhaseTime > self.yellowTime) or not self.yellow:
                nextPhaseState = self.PHASES[self.nextPhase].state
                traci.trafficlight.setRedYellowGreenState(0, nextPhaseState)
                self.currentPhase = self.nextPhase
                self.currentPhaseTime = 0
                self.yellow = False

        traci.simulationStep() 
        self.currentPhaseTime += 1
    
    def canChange(self):
        return not(self.yellow) and (self.currentPhaseTime >= self.minGreenTime)
    
    def changePhase(self, newPhase):
        if (self.currentPhase != newPhase):
            if self.canChange():
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
        self.tlPhase = tlPhase
        self.discreteLaneQueue = self.discretizeLaneInfo(lanes)
        self.discreteClass = discreteClass
        
    def getTupleState(self):
        return (self.tlPhase, self.discreteLaneQueue)
    
    def discretizeLaneInfo(self, lanes: Dict[str, Lane]):
        discreteLaneQueue: Dict[str, int] = {}
        for laneId, lane in lanes.items():
            discreteLaneQueue[laneId] = self.discrete.log_interval(lane.haltedVehicleAmount)
        return discreteLaneQueue
        
class SumoEnviroment:
    INTERSECTION_SIZE=4
    
    def __init__(self, sumocfgFile, deltaTime=3, yellowTime=3, minGreenTime=5, maxGreenTime=60, gui=False):
        self.sumocfgFile = sumocfgFile
        self.deltaTime = deltaTime
        self.trafficLight = TrafficLight("init", yellowTime, minGreenTime, maxGreenTime)
        self.gui = gui
        tls_ids = traci.trafficlight.getIDList()
        lanesIds = traci.trafficlight.getControlledLanes(tls_ids[0])

        # self.lanes = {} # Usar carriles
        self.edges: Dict[str, Lane] = {} # Usar aristas
        for laneId in lanesIds:
            if "in" in laneId:
                # Carril de entrada
                edgeId = traci.lane.getEdgeID(laneId)                     # aristas
                if edgeId not in self.edges:                              # aristas
                    self.edges[edgeId] = Lane(traci.lane.getLength(lane)) # aristas
                # self.lanes[lane] = Lane(traci.lane.getLength(lane))     # carriles   
            
        if gui:
            self.sumoBinary = checkBinary("sumo-gui")
        else:
            self.sumoBinary = checkBinary("sumo")
        
        self.discreteClass = discrete(6, 32)
        
    @property
    def observationSpace(self):
        return self.trafficLight.PHASES.keys()
       
    def initializeSimulation(self):
        sumoCMD = [self.sumoBinary, "-c", self.sumocfgFile, "--tripinfo-output", "tripinfo.xml"]
        traci.start(sumoCMD)
           
    def getCurrentState(self):
        state = State(self.trafficLight.currentPhase, self.edges, self.discreteClass)
        return state.getTupleState()
    
    def validAction(self, action):
        currentPhaseTime = self.trafficLight.currentPhaseTime
        
        return (currentPhaseTime>self.trafficLight.minGreenTime 
                & currentPhaseTime>self.trafficLight.yellowTime)
    
    def step(self, action):
        previousPhaseTime = 0
        # TOMAR ACCIÓN
        if self.validAction(action):
            previousPhaseTime = self.trafficLight.changePhase(action)
            
        # PASO DE TIEMPO (deltaTime)   
        for _ in range(self.deltaTime):
            self.trafficLight.update()
        
        for edge in self.edges.values():
            edge.update()
        
        state = self.getCurrentState()
        reward = self.computeReward()
        
    
    def reset(self):
        return null
        
        
    
                
            
          

    