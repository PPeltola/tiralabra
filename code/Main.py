from Vector import Vector
from Perceptron import Perceptron

training = []
training.append(Vector(2, arr=[1, 1]))
training.append(Vector(2, arr=[1, 0]))
training.append(Vector(2, arr=[0, 1]))
training.append(Vector(2, arr=[0, 0]))

labels = Vector(4, arr=[1, 0, 0, 0])

tron = Perceptron(1000, 0.05, 2)
tron.train(training, labels)

inputs_true = Vector(2, [1, 1])
print(tron.predict(inputs_true))

inputs_false = Vector(2, [0, 1])
print(tron.predict(inputs_false))