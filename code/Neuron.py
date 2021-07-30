from Vector import Vector

class Neuron:
    def __init__(self, input_amount, activation, activation_d, bias=1.0):
        self._weights = Vector(input_amount)
        self.activation = activation
        self.activation_d = activation_d
        self._bias = bias
    
    @property
    def weights(self):
        return self._weights
    
    @weights.setter
    def weights(self, w):
        if len(w) != len(self._weights):
            raise ValueError("Weight vector sizes are unequal!")
        self._weights = w
    
    @property
    def bias(self):
        return self._bias
    
    @bias.setter
    def bias(self, b):
        self._bias = b