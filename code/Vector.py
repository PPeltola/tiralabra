from Utils import arraycopy

class Vector:
    def __init__(self, length, default=0.0, arr=None) -> None:
        self.length = int(length)
        
        if(arr == None) or (len(arr) != length):
            self.vector = [default] * int(length)
        else:
            self.vector = arraycopy(arr)
    
    def __str__(self) -> str:
        return str(self.vector)
    
    def __getitem__(self, key):
        return self.vector[key]

    def addnum(self, x) -> None:
        for i in range(self.length):
            self.vector[i] += x

    def addvec(self, vec) -> None:
        if (self.length != vec.length):
            raise Exception("Vectors are of unequal size!")
        
        for i in range(self.length):
            self.vector[i] += vec.vector[i]
    
    def mulnum(self, x):
        for i in range(self.length):
            self.vector[i] = self.vector[i] * x
    
    def dot(self, vec) -> int:
        if (self.length != vec.length):
            raise Exception("Vectors are of unequal size!")
        
        ret = 0
        for i in range(self.length):
            ret += self.vector[i] * float(vec.vector[i])
        return ret