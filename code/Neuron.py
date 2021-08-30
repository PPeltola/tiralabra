from Vector import Vector

class Neuron:
    def __init__(self, weights, activation, activation_d, bias):
        #self.id = id
        self._weights = Vector(weights)
        self.activation = activation
        self.activation_d = activation_d
        self._bias = bias
        self.last_output = 0
    
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

    # Mainly for debugging purposes
    def __str__(self):
        opstr = ""
        opstr += "Weights: " +  str(self.weights) + "\n"
        opstr += "Bias: " + str(self.bias)# + "\n"
        #opstr += "Activation function: " + 
        return opstr
    
    def output(self, input):
        if not isinstance(input, Vector):
            raise ValueError("Given input is not a vector!")
        #print(input * self.weights)
        op = self.activation(input * self.weights + self.bias)
        self.last_output = op
        return op
    
    def adjust_weights(self, adj, rate):
        a = Vector(adj)
        self.weights = self.weights - a * rate

    def adjust_bias(self, adj, rate):
        self.bias = self.bias - adj * rate