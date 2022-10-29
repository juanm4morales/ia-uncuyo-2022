import nqueensCSP
import resultsPersistence
import time


def runSimulations(runs):
    start=0
    end=0
    algo_time=0
    sizes=[4,8,10,12,15]
    results=[]
    results.append(['Algorithm','Queens_Size','Time','States'])
    for run in range(0,runs):
        for size in sizes:
        
            rowBT=[]
            bt:nqueensCSP.NQueensCSP=nqueensCSP.NQueensCSP(size,False)
            start=time.time()
            bt.backtrackingSearch() # execution
            end=time.time()
            algo_time=end-start
            states=bt.states
            rowBT.append("backtracking")
            rowBT.append(size)
            rowBT.append(algo_time)
            rowBT.append(states)

            results.append(rowBT)
            
            rowFC=[]
            fc:nqueensCSP.NQueensCSP=nqueensCSP.NQueensCSP(size,True)
            start=time.time()
            fc.backtrackingSearch() # execution
            end=time.time()
            algo_time=end-start
            states=fc.states
            rowFC.append("forward checking")
            rowFC.append(size)
            rowFC.append(algo_time)
            rowFC.append(states)

            results.append(rowFC)
            
    return results

results=runSimulations(30)
resultsPersistence.storeResultsCSV(results)
