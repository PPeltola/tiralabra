from Utils import arraycopy

class Vector:
    def __init__(self, length, default=0.0, arr=None) -> None:
        self.length = int(length)
        
        if(arr == None) or (len(arr) != length):
            self._arr = [default] * int(length)
        else:
            self._arr = arraycopy(arr)
    
    @property
    def arr(self):
        return self._arr
    
    @arr.setter
    def arr(self, a):
        if len(a) != len(self._arr):
            raise ValueError("Given vector is not the same size!")
        self._arr = a
    
    def __str__(self) -> str:
        return str(self.arr)
    
    def __getitem__(self, key):
        return self._arr[key]
    
    def __len__(self):
        return self.length

    def __add__(self, other):
        if isinstance(other, Vector):
            if (self.length != other.length):
                raise Exception("Vectors are of unequal size!")
        
            ret = []
            for i in range(self.length):
                ret.append(self._arr[i] + other.arr[i])
            return Vector(self.length, arr=ret)
        
        else:
            ret = []
            for i in range(self.length):
                ret.append(self.arr[i] + other)
            return Vector(self.length, arr=ret)
        
    def __sub__(self, other):
        if isinstance(other, Vector):
            if (self.length != other.length):
                raise Exception("Vectors are of unequal size!")
        
            ret = []
            for i in range(self.length):
                ret.append(self._arr[i] - other.arr[i])
            return Vector(self.length, arr=ret)
        
        else:
            ret = []
            for i in range(self.length):
                ret.append(self._arr[i] - other)
            return Vector(self.length, arr=ret)

    def __mul__(self, other):
        if isinstance(other, Vector):
            if (self.length != other.length):
                raise Exception("Vectors are of unequal size!")
        
            ret = 0
            for i in range(self.length):
                ret += self._arr[i] * float(other.arr[i])
            return ret
        
        else:
            ret = []
            for i in range(self.length):
                ret.append(self._arr[i] * other)
            return Vector(self.length, arr=ret)