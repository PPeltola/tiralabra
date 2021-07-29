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
    
    def __len__(self):
        return self.length

    def addnum(self, x):
        ret = []
        for i in range(self.length):
            ret.append(self.vector[i] + x)
        return Vector(self.length, arr=ret)

    def addvec(self, vec):
        if (self.length != vec.length):
            raise Exception("Vectors are of unequal size!")
        
        ret = []
        for i in range(self.length):
            ret.append(self.vector[i] + vec.vector[i])
        return Vector(self.length, arr=ret)
    
    def mulnum(self, x):
        ret = []
        for i in range(self.length):
            ret.append(self.vector[i] * x)
        return Vector(self.length, arr=ret)
    
    def dot(self, vec) -> int:
        if (self.length != vec.length):
            raise Exception("Vectors are of unequal size!")
        
        ret = 0
        for i in range(self.length):
            ret += self.vector[i] * float(vec.vector[i])
        return ret