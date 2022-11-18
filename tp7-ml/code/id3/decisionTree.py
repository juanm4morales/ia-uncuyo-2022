import pandas as pd
import math
import os

class Node:
    def __init__(self,parent=None,value=None,children=None,label=None,classification=None):
        self.parent=parent
        self.value=value
        self.label=label
        self.children:list[Node]=children
        self.classification=classification
    
    def addChildren(self,node):
        if self.children!=None:
            self.children.append(node)
    
    def addLabel(self,label):
        self.label=label
        
    def isLeaf(self):
        if (self.children==None):
            return True
        else:
            return False
        
    def getValueNode(self,value):
        n=len(self.children)
        for i in range(0,n):
            if (self.children[i].label==value):
                return self.children[i]
        return None
        

def decisionTree(examples:pd.DataFrame,classifier):
    attributes = list(examples.columns.values)
    attributes.remove(classifier)
    
    return learnDecisionTree(examples,attributes,examples,None,classifier)

def learnDecisionTree(examples:pd.DataFrame,attributes:list,parent_examples,parent:Node,classifier):
    if examples.empty:
        return pluralityValue(parent_examples,parent,classifier)
    if sameClassification(examples,classifier):
        return pluralityValue(examples,parent,classifier)
    if len(attributes)==0:
        return pluralityValue(examples,parent,classifier)
    
    attribute = bestAttribute(examples,classifier,attributes)
    tree = Node(parent,attribute,children=[])
    values=list(examples[attribute].unique())
    for value in values:
        exs = examples.loc[examples[attribute]==value]
        attributes.remove(attribute)
        subtree:Node = learnDecisionTree(exs,attributes,examples,tree,classifier)
        attributes.append(attribute)
        #if subtree.isLeaf():
        #    print(subtree.classification)
        subtree.addLabel(value)
        tree.addChildren(subtree)
    return tree
        
    
def pluralityValue(df:pd.DataFrame,parent,classifier):
    return Node(parent,None,None,None,df[classifier].value_counts().idxmax())
    
def sameClassification(examples,classifier):
    if len(examples.groupby(["play"]))==1:
        return True
    else:
        return False

def bestAttribute(df:pd.DataFrame,classifier,attributes):
    best_a_gain=-1
    best_a = ""
    for attribute in attributes:
        a_gain=importance(df,attribute,classifier)
        if (a_gain>best_a_gain):
            best_a_gain=a_gain
            best_a=attribute
    return best_a
        
def importance(df:pd.DataFrame,attribute,classifier):
    a_val:pd.DataFrame = df.groupby([attribute,classifier]).size().reset_index(name="counts")
    p = a_val.loc[a_val["play"]=="yes","counts"].sum()
    n = a_val.loc[a_val["play"]=="no","counts"].sum()
    i=entropy(p/(p+n))
    r=remainder(a_val,classifier,attribute,p,n)
    gain=i-r
    return gain
    
def entropy(q):
    if (q==1 or q==0):
        return 0
    else:
        return -(q*math.log(q,2)+(1-q)*math.log((1-q),2))

def remainder(values:pd.DataFrame,classifier,attribute,p,n):
    size = len(values)
    rem=0
    val_list=list(values[attribute].unique())
    for val in val_list :
        pk=values.loc[(values["play"]=="yes") & (values[attribute]==val),"counts"].sum()
        nk=values.loc[(values["play"]=="no") & (values[attribute]==val),"counts"].sum()
        rem += ((pk+nk)/(p+n))*entropy((pk/(pk+nk)))
    return rem

def predict(tree:Node,dataframe:pd.DataFrame,classifier):
    size = len(dataframe)
    df=dataframe.loc[:, dataframe.columns != classifier]
    col_size=df.columns.size
    dataframe["prediction"]=""
    
    for index in df.index:
        previousNode=None
        currentNode = tree
        while currentNode != None and not(currentNode.isLeaf()):
            attr=currentNode.value
            val = df.loc[index,attr]
            previousNode = currentNode
            currentNode = currentNode.getValueNode(val)
        if currentNode!=None:
            prediction = currentNode.classification
        else: 
            print("Error in decisionTree.predict():\n   New levels not present in training data. level= ",previousNode.value)
            return False
        dataframe.at[index,"prediction"] = prediction   
    return True       

def printTree(tree:Node):
    levels=[]
    printTreeRec(tree,0,levels)
    for i in range(0,len(levels)):
        for j in range(0,len(levels[i])):
            print(levels[i][j],"_", end=" ")
        print()
    
def printTreeRec(tree:Node,lvl:int,levels:list[list]):
    levels.append([])
    if tree.parent==None:
        print("PARENT")
        print(tree.value)
        print("")
    if tree.children==None:
        return       
    for i in range(0,len(tree.children)):
        if (tree.children[i].isLeaf()):
            label="|lab="+str(tree.children[i].label)
            classification="{{"+str(tree.children[i].classification)+ "}}"
            node = label + classification
        else:
            label="|lab: "+str(tree.children[i].label)
            value=("["+str(tree.children[i].value) + "]")
            node = label + value
        printTreeRec(tree.children[i],lvl+1,levels)
        levels[lvl].append(node)
    
        