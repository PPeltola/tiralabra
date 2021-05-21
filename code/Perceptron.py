from Vector import Vector


class Perceptron:
    def __init__(self, threshold, learning_rate, input_amount, bias=0) -> None:
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
            for inputs, label in zip(training, labels):
                prediction = self.predict(inputs)
                error = (label - prediction) * self.learning_rate
                self.weights.addvec(inputs.mulnum(error))
                self.bias += error