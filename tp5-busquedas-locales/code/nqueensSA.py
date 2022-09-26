from math import exp, inf
import random
import copy

COOLING_RATE=0.9
INITIAL_TEMP=10.0
class ChessBoard:
    def __init__(self,size:int=8):
        self.size=size
        self.chessBoard=[]
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
            
    def schedule(self,t:int,temp:float):
        return temp*COOLING_RATE
            
    def simulatedAnnealing(self):
        h=self.h()
        t=0
        temp=INITIAL_TEMP
        current=self.chessBoard

        while True:
            possible=copy.deepcopy(self.chessBoard)
            temp=self.schedule(t,temp)

            if temp < 0.05:
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
            else:
                
                rdm=random.uniform(0,1)

                probability=exp(-eDiff/temp)
                #if (probability!=1):
                #    print("probability: " +str(probability))
                if rdm<probability:
                   
                    current[rc]==rr
                    h=newH
            t+=1
        return h
                    


#for i in range(0,1):                
#    chessBoard=ChessBoard()
    #print(chessBoard.chessBoard)
#    h=chessBoard.simulatedAnnealing()
    #print(h)

#print(chessBoard.chessBoard)