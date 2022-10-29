from copy import deepcopy

class Variable:
    def __init__(self, id:int, domainSize:int):
        self.id=id
        self.domainSize=domainSize
        self.domain=[i for i in range(0,domainSize)]
        self.value=None

class NQueensCSP:
    def __init__(self, size:int=8,fCheck=False):
        self.size=size
        self.variables:list[Variable]=[Variable(i,size) for i in range(0,size)]
        self.fCheck=fCheck
        self.states=0
    
    def assignmentIsComplete(self, assignment:dict[int,int]):
        return assignment.__len__()==self.size
    
    # consistent SOLO EVALUA CONSISTENCIA
    def consistent(self,var:Variable, assignment:dict[int,int]):
        i=var.id
        current=var.value
        for j in assignment.keys():
            if j==i:
                continue
            colDistance = i - j
            if assignment.get(j)==current:
                return False
            elif (assignment.get(j)==current+colDistance) or (assignment.get(j)==current-colDistance):
                return False        
        return True  
        colDistance = xi - xj
        if self.chessBoard[xj]==current:
            return False
        elif (self.chessBoard[xj]==current+colDistance) or (self.chessBoard[xj]==current-colDistance):
            return False
        return True
                
    def selectUnassignedVariable(self,variables:list[Variable]):  
        return variables.pop(0)
            
    def forwardChecking(self,var:Variable,variables:list[Variable]):
        
        previousVariables=deepcopy(variables)
        for variable in variables:
            if var.value in variable.domain:
                variable.domain.remove(var.value)
            i=var.id
            colDistance=i-variable.id
            v1=var.value+colDistance
            v2=var.value-colDistance
            if v1 in variable.domain:
                variable.domain.remove(v1)
            if v2 in variable.domain:
                
                variable.domain.remove(v2)
        return previousVariables
                
    def backtrackingSearch(self):
        assignment={}
        variables = deepcopy(self.variables)
        return self.chessBoard(self.backtrack(assignment,variables))
    
    def backtrack(self,assignment:dict[int,int],variables):
        if self.assignmentIsComplete(assignment):
            return assignment
        var:Variable = self.selectUnassignedVariable(variables)
        for value in var.domain:
            var.value=value
            self.states+=1
            if self.consistent(var,assignment):
                
                assignment[var.id]=value
                if self.fCheck:
                    previousVariables=self.forwardChecking(var,variables)
                
                result = self.backtrack(assignment,variables)
                if result != None:
                    return result
                if self.fCheck:
                    variables=previousVariables
                assignment.pop(var.id)
        variables.insert(0, var)
        return None
        
    def chessBoard(self, assignment:dict[int,int]):
        if assignment==None:
            return None
        chessBoard=[]
        for key in assignment.keys():
            chessBoard.insert(key, assignment[key])
        return chessBoard

    def reset(self):
        self.states=0

