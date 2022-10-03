from threading import local
import nqueensGA as nqGA
import nqueensSA as nqSA
import nqueensHC as nqHC
import resultsPersistence
import time

class NQueensSimulation:
    
    def __init__(self, runs:int=30):
        self.runs=runs
        self.boardSizes=[4,8,10,12,15]
        self.nqueens=[]
        for i in range(0,len(self.boardSizes)):
            row=[]
            nqueensHC=nqHC.NQueensHC(self.boardSizes[i])
            nqueensSA=nqSA.NQueensSA(self.boardSizes[i])
            nqueensGA=nqGA.NQueensGA(self.boardSizes[i])
            row.append(nqueensHC)
            row.append(nqueensSA)
            row.append(nqueensGA)
            self.nqueens.append(row)
            
    def runSimulations(self):
        start=0
        end=0
        algo_time=0
        results=[]
        results.append(['Algorithm','Queens_Size','Time','States','Optimal_solution'])
        for run in range(0,self.runs):
            for bs in range(0,len(self.nqueens)):
                
                # Hill Climbing solution                
                rowHC=[]
                hc:nqHC.NQueensHC=self.nqueens[bs][0]
                start=time.time()
                hHC=hc.hillClimbing() # execution
                end=time.time()
                algo_time=end-start
                states=len(hc.hFunc)
                rowHC.append("hill_climbing")
                rowHC.append(self.boardSizes[bs])
                rowHC.append(algo_time)
                rowHC.append(states)
                rowHC.append(str(hHC==0))
                results.append(rowHC)
                
                # Simulated Annealing solution
                rowSA=[]
                sa:nqSA.NQueensSA=self.nqueens[bs][1]
                start=time.time()
                hSA=sa.simulatedAnnealing() # execution
                end=time.time()
                algo_time=end-start
                states=len(sa.hFunc)
                rowSA.append('simulated_annealing')
                rowSA.append(self.boardSizes[bs])
                rowSA.append(algo_time)
                rowSA.append(states)
                rowSA.append(str(hSA==0))
                results.append(rowSA)

                # Genetic Algorithm solution
                rowGA=[]
                ga:nqGA.NQueensGA=self.nqueens[bs][2]
                start=time.time()
                hGA=ga.geneticAlgorithm() # execution
                end=time.time()
                algo_time=end-start
                states=len(ga.hFunc)
                rowGA.append('genetic_algorithm')
                rowGA.append(self.boardSizes[bs])
                rowGA.append(algo_time)
                rowGA.append(states)
                rowGA.append(len(hGA)!=0)
                results.append(rowGA)
                
                hc.reset()
                sa.reset()
                ga.reset()
                
                print("run="+str(run+1))
        return results
    
nqueens=NQueensSimulation(30)
results=nqueens.runSimulations()
resultsPersistence.storeResultsCSV(results)
                

