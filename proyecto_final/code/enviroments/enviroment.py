import traci
from sumolib import checkBinary

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
        
class LaneQueue:
    def __init__(self, laneLength):
        self.vehicles = []
        # self.congestion_lvl = 0
        self.laneLength = laneLength
        
    def addVehicle(self, vehicle):
        self.vehicles.append(vehicle)
        
    def getTotalWaitingTime(self):
        return sum(vehicle.waitingTime for vehicle in self.vehicles)
    
    def getAvgWaitingTime(self):
        return self.getTotalWaitingTime() / len(self.vehicles)
        
        
class TrafficLight:
    def __init__(self, initialPhase, yellowTime, minGreenTime, maxRedTime):
        self.currentPhase = initialPhase
        self.nextPhase = initialPhase
        self.yellowTime = yellowTime
        self.minGreenTime = minGreenTime
        self.maxRedTime = maxRedTime
        self.yellowTransition = 0
        
    def updatePhase(self):
        if (self.currentPhase != self.nextPhase):
            if self.yellowTime > 0:
                self.yellowTime -= 1
            else:
                self.currentPhase = self.nextPhase

class SumoEnviroment:
    def __init__(self, sumocfgFile, deltaTime, yellowTime, minGreenTime, maxRedTime, gui):
        self.sumocfgFile = sumocfgFile
        self.deltaTime = deltaTime
        self.trafficLight = TrafficLight("", yellowTime, minGreenTime, maxRedTime)
        
        self.minGreenTime = minGreenTime
        self.maxRedTime = maxRedTime
        self.gui = gui
        # FALTA inicializar colas de vehículos en carriles
        if gui:
            self.sumoBinary = checkBinary("sumo-gui")
        else:
            self.sumoBinary = checkBinary("sumo")
        
    def initializeSimulation(self):
        sumoCMD = [self.sumoBinary, "-c", self.sumocfgFile, "--tripinfo-output", "tripinfo.xml"]
        traci.start(sumoCMD)
    
    def step(self, action):
        traci.simulationStep()
        
        
        
    
                
            
          

    