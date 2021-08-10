from HiddenLayer import HiddenLayer
from Vector import Vector
from Neuron import Neuron
#from Perceptron import Perceptron
import IO
import UI
import Loss
import Utils
import Activation
import Backpropagation


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

# Vector multiplication test
""" print(Vector(4, arr=[1, 2, 3, 4]) * Vector(4, arr=[1, 2, 2, 2])) """

# Neuron output test
""" n = Neuron(Utils.rand_array(4), Activation.sigmoid, Activation.sigmoid_d, 3)
x = Vector(4, arr=Utils.rand_array(4))
print(n)
print(x)
print(n.output(x)) """

# rand_array and normalization test
""" arr = Utils.rand_array(10, -5, 15)
print(arr)
print(Utils.normalize(arr, -5, 15)) """

# Testing some hidden layer basic functionality and saving/loading
""" images = IO.read_images('test')
labels = IO.read_labels('test')

weights = [Utils.rand_array(784, -1, 1) for _ in range(10)]
hl_a = HiddenLayer(10, 784, weights,  Activation.sigmoid, Activation.sigmoid_d, Loss.quadratic, Loss.quadratic_d, 0.1)

#IO.save_layer(hl_a, "test")
hl_b = IO.load_layer("test")

for i in range(9):
    img = Vector(Utils.normalize(Utils.flatten_2d(images[i]), 0, 255))
    o1 = hl_a.generate_output(img)
    o2 = hl_b.generate_output(img)
    #print("Picture " + str(i + 1) + ": " + str(o1) + ", " + str(o2) + ", correct answer is " + str(labels[i]))
    print(o1)
    print(o2) """

# Array flattening testing
""" testarr = [[1, 2, 7, 8], [3, 4, 9, 10], [5, 6, 11, 12]]
testarr = Utils.flatten_2d(testarr)
print(testarr)
testarr = Utils.deflatten_2d(testarr, 4, 3)
print(testarr) """

# Let's test multi-layer nets
""" images = IO.read_images('test')
labels = IO.read_labels('test')
img_test = images[:20]
lab_test = labels[:20]

weights_a = [Utils.rand_array(784, 0, 1) for _ in range(10)]
weights_b = [Utils.rand_array(10, 0, 1) for _ in range(10)]
hl_a = HiddenLayer(10, 784, weights_a,  Activation.sigmoid, Activation.sigmoid_d, Loss.quadratic, Loss.quadratic_d, 0.1)
hl_b = HiddenLayer(10, 10, weights_b,  Activation.sigmoid, Activation.sigmoid_d, Loss.quadratic, Loss.quadratic_d, 0.1)

LEARNING_RATE = 0.5

for (i, l) in zip(images, labels):
    img = Vector(Utils.normalize(Utils.flatten_2d(i), 0, 255))
    lab = Utils.onehot_label_arr(l)
    o_a = hl_a.generate_output(img)
    o_b = hl_b.generate_output(o_a)
    grads = Backpropagation.output_layer_grads(hl_b, o_b, lab, hl_a, LEARNING_RATE)
    #grad_b = 
    #print("Picture " + str(i + 1) + ": " + str(o1) + ", " + str(o2) + ", correct answer is " + str(labels[i]))
    #print(o_a)
    #print(o_b)
    #print(lab)
    #print()
    #print("----")

for n in hl_b.neurons:
    print(n.weights) """

# Let's try how well a single one-layer 10-neuron net performs!
images = IO.read_images('training')
labels = IO.read_labels('training')

test_images = IO.read_images('test')
test_labels = IO.read_labels('test')

weights_a = [Utils.rand_array(784, 0, 1) for _ in range(10)]
hl_a = HiddenLayer(10, 784, weights_a,  Activation.sigmoid, Activation.sigmoid_d, Loss.quadratic, Loss.quadratic_d, 0.1)

LEARNING_RATE = 0.05

j = 1
for (i, l) in zip(images, labels):
    img = Vector(Utils.normalize(Utils.flatten_2d(i), 0, 255))
    lab = Utils.onehot_label_arr(l)
    o_a = hl_a.generate_output(img)
    grads = Backpropagation.single_layer_grads(hl_a, o_a, lab, img, LEARNING_RATE)
    
    if j % 1000 == 0:
        print(j)
    j += 1

right_amount = 0
for (i, l) in zip(test_images, test_labels):
    img = Vector(Utils.normalize(Utils.flatten_2d(i), 0, 255))
    o_a = hl_a.generate_output(img)
    pred = Utils.make_prediction(o_a)
    if pred == l:
        right_amount += 1

print(right_amount / 10000)