import math
import random

import matplotlib.pyplot as plt

class NQueensHC:
    def __init__(self,size:int=8):
        self.hFunc=[]
        self.states:int=0
        self.size=size
        self.chessBoard=[]
        for i in range(size):
            self.chessBoard.append(random.randint(0,size-1))

    def h(self):
        h=0
        for i in range(0,self.size):
            current=self.chessBoard[i]
            for j in range(0,self.size):
                if j==i:
                    continue
                colDistance = i - j
                if self.chessBoard[j]==current:
                    h=h+1
                elif (self.chessBoard[j]==current+colDistance) or (self.chessBoard[j]==current-colDistance):
                    h=h+1
        return h/2
                
    def createBoard(self):
        board:list[list[int]]=[]
        for i in range(0,self.size):
            board.append([])
            for j in range(0,self.size):
                board[i].append(math.inf)
                
        return board

    def printMatrix(self, matrix):
        n=len(matrix)
        for r in range(0,n):
            print("|",end="")
            for c in range(0,len(matrix[r])):
                print(str(matrix[r][c])+"|",end="")
            print("")
            
    def fillPossibleStatesCol(self, possibleStates:list[list[int]], row:int, col:int):
        # min Possible h
        minPH=possibleStates[row][col]
        bestMoves=[row]
        for r in range(0,self.size):
            if r!=row:
                self.chessBoard[col]=r
                pH=self.h()
                if pH<=minPH:                  
                    if pH<minPH:
                        minPH=pH
                        bestMoves=[r]
                    else:
                        bestMoves.append(r)
                    
                possibleStates[r][col]=pH
        self.chessBoard[col]=row
        return (minPH, col, bestMoves)
    
            
    def hillClimbing(self):
        it=0
        h=self.h()
        self.hFunc.append(h)
        possibleStates=self.createBoard()
        bestMoves:list[(float,int,list[int])]=[]
        minPHCol=math.inf
        while h!=0:
            bestMoves=[]
            # Generate possible states
            for k in range(0,self.size):
                possibleStates[self.chessBoard[k]][k]=h
            
            for col in range(0,self.size):
                row=self.chessBoard[col]
                # Just the best moves in a column are chosen
                bestMovesCol=self.fillPossibleStatesCol(possibleStates, row, col)
                bestMoves.append(bestMovesCol)
                bestMoves.sort() # Can be optimized by putting the lowest value, so far, at the beginning.

            # Only the best moves from all columns are selected
            minPH=bestMoves[0][0]
            col=0
            while col<len(bestMoves):
                bestMovesCol=bestMoves[col]
                if bestMovesCol[0] > minPH:
                    bestMoves.pop(col)
                else:
                    col=col+1

            # One of the best possible moves is selected randomly
            r1=random.randint(0, len(bestMoves)-1)
            r2=random.randint(0, len(bestMoves[r1][2])-1)
            selectedRow=bestMoves[r1][2][r2]
            selectedCol=bestMoves[r1][1]
            self.chessBoard[selectedCol]=selectedRow
            nextH=bestMoves[r1][0]
            it=it+1
            if nextH>=h:
                return h
            h=nextH
            self.hFunc.append(h)
            #print(h)
        return h

    def reset(self):
        self.hFunc=[]
        self.states:int=0
        self.chessBoard=[]
        for i in range(self.size):
            self.chessBoard.append(random.randint(0,self.size-1))