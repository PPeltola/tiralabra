from Vector import Vector
from Utils import arraycopy

class Perceptron:
    def __init__(self, input_amount, threshold, learning_rate, bias=0.0) -> None:
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = Vector(input_amount)
        self.bias = bias

    def predict(self, inputs):
        dotsum = inputs.dot(self.weights) + self.bias

        if dotsum > 0:
          return 1
        return 0

    def train(self, training, labels):
        for i in range(self.threshold):
            for (inputs, label) in zip(training, labels):
                icopy = Vector(2, arr=inputs.vector)
                prediction = self.predict(icopy)
                error = (label - prediction) * self.learning_rate
                #print("inputs: " + str(icopy) + " label: " + str(label) + " prediction: " + str(prediction))
                icopy.mulnum(error)
                self.weights.addvec(icopy)
                self.bias += error
                #print("weights: " + str(self.weights) + " bias: " + str(self.bias) + " error: " + str(error))