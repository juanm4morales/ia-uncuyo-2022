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
    class Phase:
        def __init__(self, state, yellowTransition):
            self.state = state
            self.yellowTransition = yellowTransition
            
        
    # n=north, s=south, e=east, w=weast, l=left turn allowed (without priority)
    # G=Green with priority, g=green without priority, y=yellow, r=red
    PHASES = {'ns_sn_l':    Phase("GGGgrrrrGGGgrrrr", "yyyyrrrryyyyrrrr"),
              'ew_we_l':    Phase("rrrrGGGgrrrrGGGg", "rrrryyyyrrrryyyy"),
              'sn':         Phase("rrrrrrrrGGGGrrrr", "rrrrrrrryyyyrrrr"),
              'ns':         Phase("GGGGrrrrrrrrrrrr", "yyyyrrrrrrrrrrrr"),
              'we':         Phase("rrrrrrrrrrrrGGGG", "rrrrrrrrrrrryyyy"),
              'ew':         Phase("rrrrGGGGrrrrrrrr", "rrrryyyyrrrrrrrr"),
              'ns_sn':      Phase("GGGrrrrrGGGrrrrr", "yyyrrrrryyyrrrrr"),
              'ew_we':      Phase("rrrrGGGrrrrrGGGr", "rrrryyyrrrrryyyr")
              }
    
    def __init__(self, id, initialPhase, yellowTime, minGreenTime, maxGreenTime):
        self.id = id
        self.currentPhase = initialPhase
        self.nextPhase = initialPhase
        self.yellowTime = yellowTime
        self.minGreenTime = minGreenTime
        self.maxGreenTime = maxGreenTime
        self.yellowTransition = 0
        self.currentPhaseTime = 0
        
    def update(self):
        if (self.currentPhase != self.nextPhase):
            if self.yellowTransition > 0:
                self.yellowTransition -= 1
            else:
                self.currentPhase = self.nextPhase
        self.currentPhaseTime += 1
    
    def changePhase(self, newPhase):
        if (self.currentPhase != newPhase):
            if (self.currentPhaseTime > self.minGreenTime):
                phaseObject = self.PHASES[self.changePhase]
                yellowPhase = phaseObject.yellowTransition
                self.yellowTransition = self.yellowTime
                self.currentPhase = yellowPhase
                self.currentPhaseTime=0
                self.nextPhase = newPhase
                return self.currentPhaseTime
            else:
                # No ha pasado el mínimo de tiempo de duración de la fase
                return -1
        else:
            # La fase actual es la misma que la nueva
            return -2
            

class SumoEnviroment:
    INTERSECTION_SIZE=4
    
    def __init__(self, sumocfgFile, deltaTime, yellowTime, minGreenTime, maxGreenTime, gui):
        self.sumocfgFile = sumocfgFile
        self.deltaTime = deltaTime
        self.trafficLight = TrafficLight("rrrrrrrrrrrrrrrr", yellowTime, minGreenTime, maxGreenTime)
        self.gui = gui
        
        tls_ids = traci.trafficlight.getIDList()
        lanes = traci.trafficlight.getControlledLanes(tls_ids[0])
        maxLaneLength = 0
        for lane in lanes:
            if traci.lane.getLength(lane) > maxLaneLength:
                maxLaneLength = traci.lane.getLength(lane)
            
        
        for i in range(self.INTERSECTION_SIZE):
            # Para un solo controlador de semáforo   
            lanes[i] = LaneQueue(maxLaneLength)
            
            
           
        # FALTA inicializar colas de vehículos en carriles
        if gui:
            self.sumoBinary = checkBinary("sumo-gui")
        else:
            self.sumoBinary = checkBinary("sumo")
        
    def initializeSimulation(self):
        sumoCMD = [self.sumoBinary, "-c", self.sumocfgFile, "--tripinfo-output", "tripinfo.xml"]
        traci.start(sumoCMD)
    
    def step(self, action):
        self.trafficLight.changePhase(action)
        self.trafficLight.update()
        traci.simulationStep()
        # Retornar estado y recompensa
        
        
        
    
                
            
          

    