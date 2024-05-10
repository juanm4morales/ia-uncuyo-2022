from math import ceil, log2

class discrete:
    def __init__(self, I, M):
        self.I=I-1
        self.M=M
        self.L=self.I/self.M
        self.F=(1-self.L)*(self.I/(log2(M/(M*self.L)+1)))
             
    def log_interval(self, x):
        print(self.I)
        interval = ceil(self.F*(log2(x/(self.M*self.L)+1))+pow(self.L,2)*x)
        return interval

