from Vector import Vector
from Neuron import Neuron

class HiddenLayer:
    def __init__(self, size, input_size, weights, activation, activation_d, loss, loss_d, bias=1.0):
        self.size = size
        #self.input_layer = input_layer
        self.input_size = input_size
        #self.output_layer = output_layer
        self.loss = loss
        self.loss_d = loss_d
        self._neurons = []

        for w in weights:
            if len(w) != self.input_size:
                raise ValueError("Mismatched weight and input size!")

            self._neurons.append(Neuron(w, activation, activation_d, bias))
    
    @property
    def neurons(self):
        return self._neurons

    @neurons.setter
    def neurons(self, n):
        self._neurons = n

    def __getitem__(self, key):
        return self._neurons[key]
    
    def __len__(self):
        return self.size
        
    def generate_output(self, input):
        if len(input) != self.input_size:
            raise ValueError("Input is not of the defined length!")
        
        op = []
        lin = []
        for n in self._neurons:
            output = n.output(input)
            op.append(output['op'])
            lin.append(output['lin'])
        return {'op':Vector(op), 'lin':Vector(lin)}