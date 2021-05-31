from Vector import Vector
from Perceptron import Perceptron


# As a test, let's simulate the OR-gate
training = []
training.append(Vector(2, arr=[1, 1]))
training.append(Vector(2, arr=[1, 0]))
training.append(Vector(2, arr=[0, 1]))
training.append(Vector(2, arr=[0, 0]))

labels = Vector(4, arr=[1, 1, 1, 0])

tron = Perceptron(2, 100, 0.05)
tron.train(training, labels)

both_true = Vector(2, arr=[1, 1])
right_true = Vector(2, arr=[0, 1])
left_true= Vector(2, arr=[1, 0])
both_false = Vector(2, arr=[0, 0])

print(tron.predict(both_true))
print(tron.predict(right_true))
print(tron.predict(left_true))
print(tron.predict(both_false))