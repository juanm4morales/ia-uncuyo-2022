import csv
import os

def storeResultsCSV(rows:list[list[object]]):
    
    fileName = 'results.csv'
    currentPath = os.path.dirname(__file__)
    parentPath = os.path.dirname(currentPath)
    path=os.path.join(parentPath,fileName)
    csvfile=open(path, 'w', newline="")
    writer = csv.writer(csvfile)
    writer.writerows(rows)
    csvfile.close()

def loadResults()->list[list[object]]:
    
    fileName = 'results.csv'
    currentPath = os.path.dirname(__file__)
    parentPath = os.path.dirname(currentPath)
    path=os.path.join(parentPath,fileName)
    
    csvfile=open(path, 'r')
    reader = csv.reader(csvfile)
    results=[]
    for row in reader:
        results.append(row)
        
    return results