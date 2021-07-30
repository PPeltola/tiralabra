from Vector import Vector
from Perceptron import Perceptron
import Data
import UI
import Loss


# As a test, let's simulate the OR-gate with a single perceptron
""" training = []
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
print(tron.predict(both_false)) """

# Testing the reading of data
""" images = Data.read_images('test')
labels = Data.read_labels('test')

UI.draw_image(images[1234], "testi")
print(labels[1234]) """

print(Vector(4, arr=[1, 2, 3, 4]) * Vector(4, arr=[1, 2, 2, 2]))