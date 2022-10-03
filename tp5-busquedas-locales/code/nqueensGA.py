from math import exp, inf
import random
import copy
import numpy

import matplotlib.pyplot as plt

MUTATION_RATE=0.05

class ChessBoard:
    def __init__(self, size:int=8, rdm:bool=True):
        self.size=size
        self.chessBoard=[]
        if rdm:
            for i in range(0,size):
                self.chessBoard.append(random.randint(0,self.size-1))
        else:
            for i in range(0,size):
                self.chessBoard.append(0)
        self.fitness:float=None
        
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
        self.fitness=h/2
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
            
class NQueensGA:
    def __init__(self, boardSize:int=8):
        self.boardSize=boardSize
        self.popSize=boardSize*(boardSize-1)
        self.population:list[ChessBoard]=[]
        weights=[]
        weightSum=0
        minH=inf #used for results
        for i in range(0, self.popSize):
            chessBoard=ChessBoard(boardSize)
            self.population.append(chessBoard)
            h=chessBoard.h() 
            if h<minH: 
                minH=h
            if (h!=0):
                w=(1/h)
            else:
                w=10
            weights.append(w)
            weightSum+=w
        self.hFunc=[] #used for results
        self.hFunc.append(int(minH))
        self.probabilities=[(w/weightSum) for w in weights]
    
    def randomParentsPickup(self,population:list[ChessBoard], probabilites:list[float]):
        parents = numpy.random.choice(population, 2, False, probabilites)
        return parents
            
    def singlePointCrossover(self, x:ChessBoard, y:ChessBoard):
        
        offspring1=ChessBoard(self.boardSize)
        offspring2=ChessBoard(self.boardSize)
        
        point = random.randint(0,self.boardSize-1)
        
        i=0
        while (i<point):
            offspring1.chessBoard[i]=x.chessBoard[i]
            offspring2.chessBoard[i]=y.chessBoard[i]
            i+=1
        j=i
        while (j<self.boardSize):
            offspring1.chessBoard[j]=y.chessBoard[j]
            offspring2.chessBoard[j]=x.chessBoard[j]
            j+=1
        return (offspring1,offspring2)
    
    def mutate(self, offspring:ChessBoard):
        # 1/ChessBoardSize is the probability that there is no mutation
        offspring.chessBoard[random.randint(0,self.boardSize-1)]=random.randint(0,self.boardSize-1)
    
    def updatePopulationData(self):
        weightSum=0
        weights=[]
        minH=inf # used for results
        for i in range(0, self.popSize):
            chessBoard=self.population[i]
            if (chessBoard.fitness<minH):
                minH=chessBoard.fitness
            if (chessBoard.fitness!=0):
                w=(1/chessBoard.fitness)
            else:
                w=10
            weights.append(w)
            weightSum+=w
        self.hFunc.append(int(minH))
        self.probabilities=[(w/weightSum) for w in weights]
        return minH

    def geneticAlgorithm(self):
        t=0
        done=False
        solution=set()
        generation=0
        minHAchieved=inf
        stuckness=0
        maxStuckness=self.popSize*10
        mutationRate=MUTATION_RATE
        while not(done):
            newPopulation:list[ChessBoard]=[]
            hashList=[]
            while len(newPopulation)<self.popSize:
                parents = self.randomParentsPickup(self.population, self.probabilities)
                offsprings:tuple[ChessBoard,ChessBoard] = self.singlePointCrossover(parents[0],parents[1])
                offspring1=offsprings[0]
                offspring2=offsprings[1]
                
                # p = MUTATION_RATE probability of mutatation
                
                if random.uniform(0,1)<=mutationRate:
                    self.mutate(offspring1)

                if random.uniform(0,1)<=mutationRate:
                    self.mutate(offspring2)     
                
                h1=offspring1.h()
                h2=offspring2.h()
                
                offspring1Hash=hash(tuple(offspring1.chessBoard))
                offspring2Hash=hash(tuple(offspring2.chessBoard))
                
                if offspring1Hash not in (hashList):
                    newPopulation.append(offspring1)
                    hashList.append(offspring1Hash)
                    
                if (offspring2Hash not in (hashList)) and (len(newPopulation)<self.popSize):
                    newPopulation.append(offspring2)
                    hashList.append(offspring2Hash) 

                if h1==0:
                    solution.add(tuple(offspring1.chessBoard))
                    done=True
                if h2==0:
                    solution.add(tuple(offspring2.chessBoard))
                    done=True
                    
            self.population=newPopulation
            minHPop=self.updatePopulationData()
            # <jam handler>
            if stuckness>=maxStuckness:
                if stuckness==maxStuckness:
                    mutationRate=mutationRate*2
                elif stuckness==maxStuckness*2:
                    mutationRate=mutationRate*2
                elif stuckness==maxStuckness*3:
                    mutationRate=mutationRate*2
            if minHPop<minHAchieved:
                minHAchieved=minHPop
                mutationRate=MUTATION_RATE
                stuckness=0
            else:
                stuckness+=1
            # </jam handler>
            generation+=1
        return solution
    
    def reset(self):
        self.population=[]
        self.probabilities=[]
        weights=[]
        weightSum=0
        minH=inf #used for results
        for i in range(0, self.popSize):
            chessBoard=ChessBoard(self.boardSize)
            self.population.append(chessBoard)
            h=chessBoard.h() 
            if h<minH: 
                minH=h
            if (h!=0):
                w=(1/h)
            else:
                w=10
            weights.append(w)
            weightSum+=w
        self.hFunc=[] #used for results
        self.hFunc.append(int(minH))
        self.probabilities=[(w/weightSum) for w in weights]
