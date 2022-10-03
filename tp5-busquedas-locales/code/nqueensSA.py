from math import exp, inf
import random
import copy
import numpy
import time
import matplotlib.pyplot as plt

COOLING_RATE=0.9
INITIAL_TEMPETURE=4.0
class NQueensSA:
    def __init__(self,size:int=8):
        self.size=size
        self.chessBoard=[]
        self.hFunc=[] #used for results
        for i in range(size):
            self.chessBoard.append(random.randint(0,size-1))

    def h(self, chessBoard:list[int]=None):
        if chessBoard==None:
            chessBoard=self.chessBoard
        h=0
        for i in range(0,self.size):
            current=chessBoard[i]
            for j in range(0,self.size):
                if j==i:
                    continue
                colDistance = i - j
                if chessBoard[j]==current:
                    h=h+1
                elif (chessBoard[j]==current+colDistance) or (chessBoard[j]==current-colDistance):
                    h=h+1
        return h/2

    def createBoard(self):
        board:list[list[int]]=[]
        for i in range(0,self.size):
            board.append([])
            for j in range(0,self.size):
                board[i].append(inf)
                
        return board

    def printMatrix(self, matrix):
        n=len(matrix)
        for r in range(0,n):
            print("|",end="")
            for c in range(0,len(matrix[r])):
                print(str(matrix[r][c])+ "|",end="")
            print("")
    
    def schedule(self,t:int,tMax:float,steps:int,temp:float=None):
        #return tMax/(t+1)
        return tMax*((steps-t)/steps)**2
        #return temp*COOLING_RATE
        #return tMax*(1/(1+exp((2*numpy.log(tMax)/steps)*(t-0.5*steps))))
        #return tMax*((steps-t)/steps)**2
        #return 50/(1+0.01*t**2)
            
    def simulatedAnnealing(self):
        h=self.h()
        self.hFunc.append(h) #used for results
        n = int((10/4)*self.size**3)
        current=self.chessBoard
        maxTemp=INITIAL_TEMPETURE
        t=0
        
        while h!=0 and t<n:
            
            possible=copy.deepcopy(self.chessBoard)
            temp=self.schedule(t,maxTemp,n)
            
            if temp==0:
                print("IN")
                return h
            rc=random.randint(0,self.size-1)
            rr=current[rc]
            while rr==current[rc]:
                rr=random.randint(0,self.size-1)

            possible[rc]=rr
            newH=self.h(possible)

            eDiff=newH-h
            if eDiff<0:
                current[rc]=rr
                h=newH     
            
            elif eDiff>0:
                rdm=random.uniform(0,1)
                probability=exp(-eDiff/temp)
                
                if rdm<probability:    
                    current[rc]==rr
                    h=newH
            self.hFunc.append(h) #used for results
            t+=1
            
        return h
                    
    def reset(self):
        self.chessBoard=[]
        self.hFunc=[] #used for results
        for i in range(self.size):
            self.chessBoard.append(random.randint(0,self.size-1))