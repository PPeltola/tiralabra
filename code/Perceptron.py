from Activation import heaviside
from Vector import Vector
#from Utils import arraycopy

class Perceptron:
    def __init__(self, input_amount, threshold, learning_rate, bias=0.0, activation=heaviside):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = Vector(input_amount)
        self.bias = bias
        self.activation = activation

    def predict(self, inputs):
        return self.activation(inputs.dot(self.weights) + self.bias)

    def train(self, training, labels):
        for i in range(self.threshold):
            for (inputs, label) in zip(training, labels):
                icopy = Vector(2, arr=inputs.vector)
                prediction = self.predict(icopy)
                error = (label - prediction) * self.learning_rate
                #print("inputs: " + str(icopy) + " label: " + str(label) + " prediction: " + str(prediction))
                icopy = icopy.mulnum(error)
                self.weights = self.weights.addvec(icopy)
                self.bias += error
                #print("weights: " + str(self.weights) + " bias: " + str(self.bias) + " error: " + str(error))