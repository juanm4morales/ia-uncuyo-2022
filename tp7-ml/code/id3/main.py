import pandas as pd
from decisionTree import *
from sklearn.metrics import accuracy_score

fileName = "tennis.csv"
currentPath = os.path.dirname(__file__)
path=os.path.join(currentPath,fileName)
data = pd.read_csv(path)

n=1000
i=0
sum=0
while i<n:
    train = data.sample(frac=0.8)
    test = data.drop(train.index)
    tree=decisionTree(train,"play")
    canPredict=predict(tree,test,"play")
    if canPredict:
        y_true=test["play"].tolist()
        y_pred=test["prediction"].tolist()
        acc=accuracy_score(y_true,y_pred)
        sum+=acc
        i=i+1
        
avg_acc=sum/n
print("Average accuracy: ",avg_acc)