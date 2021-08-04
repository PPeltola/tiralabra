# This class may actually be useless, at least for now

class InputLayer:
    def __init__(self, size, data):
        self.size = size
        self.data = data
        self.i = 0
    
    def next(self):
        if self.i <= len(self.data) - 1:
            d = self.data[self.i]
            self.i += 1
            return d
        else:
            raise RuntimeError("Out of input data!")