import csv

def storeResultsCSV(rows:list[list[object]]):

    csvfile=open('results.csv', 'w', newline="")
    writer = csv.writer(csvfile)
    writer.writerows(rows)
    csvfile.close()

def loadResults()->list[list[object]]:
    csvfile=open('results.csv', 'r')
    reader = csv.reader(csvfile)
    results=[]
    for row in reader:
        results.append(row)
        
    return results