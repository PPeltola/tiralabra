from HiddenLayer import HiddenLayer
from Vector import Vector
from Neuron import Neuron
#from Perceptron import Perceptron
import IO
#import UI
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
# Read images and labels
""" images = IO.read_images('training')
labels = IO.read_labels('training')
test_images = IO.read_images('test')
test_labels = IO.read_labels('test')
print("Images & labels read!")

# Preprocess images and labels
images_flat = []
labels_oh = []
test_images_flat = []

for (i, l) in zip(images, labels):
    images_flat.append(Vector(Utils.normalize(Utils.flatten_2d(i), 0, 255)))
    labels_oh.append(Utils.onehot_label_arr(l))

for i in test_images:
    test_images_flat.append(Vector(Utils.normalize(Utils.flatten_2d(i), 0, 255)))

print("Images & labels processed!")

# Initialize weights and layer
#weights_a = [Utils.rand_array(784, 0, 1) for _ in range(10)]
weights_a = [[0] * 784] * 10
hl_a = HiddenLayer(10, 784, weights_a,  Activation.sigmoid, Activation.sigmoid_d, Loss.quadratic, Loss.quadratic_d, 0.1)

LEARNING_RATE = 0.05

iter = 1
prev_correct = 0
#old_weights = weights_a
while True:
    print("Iteration: " + str(iter))

    j = 1
    for (img, lab) in zip(images_flat, labels_oh):
        o_a = hl_a.generate_output(img)
        grads = Backpropagation.output_layer_backpropagate(hl_a, o_a, lab, img, LEARNING_RATE)
    
        if j % 1000 == 0:
            print("    " + str(j))
        j += 1

    right_amount = 0
    for (img, lab) in zip(test_images_flat, test_labels):
        o_a = hl_a.generate_output(img)
        pred = Utils.make_prediction(o_a)
        if pred == lab:
            right_amount += 1
    
    print("Correct predictions: " + str(right_amount))

    if (iter > 10):
        break

    prev_correct = right_amount
    iter = iter + 1 """

#IO.save_layer(hl_a, "test1_3")



# Visualize weights!
""" hl_a = IO.load_layer("test1_3")

i = 0
for n in hl_a.neurons:
    weights = n.weights
    weights = Utils.fit_arr(weights, 0, 255)
    #print(weights)
    IO.save_image(Utils.deflatten_2d(weights, 28, 28), "w" + str(i))
    i += 1 """



# Final boss: a 16-16-10 multi-layer net!
images = IO.read_images('training')
labels = IO.read_labels('training')
test_images = IO.read_images('test')
test_labels = IO.read_labels('test')
print("Images & labels read!")

# Preprocess images and labels
images_flat = []
labels_oh = []
test_images_flat = []

for (i, l) in zip(images, labels):
    images_flat.append(Vector(Utils.normalize(Utils.flatten_2d(i), 0, 255)))
    #images_flat.append(Vector(Utils.flatten_2d(i)))
    labels_oh.append(Utils.onehot_label_arr(l))

for i in test_images:
    test_images_flat.append(Vector(Utils.normalize(Utils.flatten_2d(i), 0, 255)))
    #test_images_flat.append(Vector(Utils.flatten_2d(i)))

print("Images & labels processed!")

# Initialize weights and layer
#weights748_16 = [[0.5] * 784] * 16
#weights16_16 = [[0.5] * 16] * 16
#weights16_10 = [[0.5] * 16] * 10
weights748_16 = [Utils.rand_array(784, 0, 1) for _ in range(16)]
weights16_16 = [Utils.rand_array(16, 0, 1) for _ in range(16)]
weights16_10 = [Utils.rand_array(16, 0, 1) for _ in range(10)]

hl_a = HiddenLayer(16, 784, weights748_16,  Activation.relu, Activation.relu_d, Loss.quadratic, Loss.quadratic_d, 0.1)
hl_b = HiddenLayer(16, 16, weights16_16,  Activation.sigmoid, Activation.sigmoid_d, Loss.quadratic, Loss.quadratic_d, 0.1)
opl = HiddenLayer(10, 16, weights16_10,  Activation.sigmoid, Activation.sigmoid_d, Loss.quadratic, Loss.quadratic_d, 0.1)

ITERATION_CAP = 5
ACCURACY_CAP = 9800

LEARNING_RATE = 0.1
BATCH_SIZE = 30

iter = 1
prev_correct = 0
#old_weights = weights
while True:
    print("Iteration: " + str(iter))

    j = 1
    for (img, lab) in zip(images_flat, labels_oh):
        o_a = hl_a.generate_output(img)
        o_b = hl_b.generate_output(o_a)
        output = opl.generate_output(o_b)
        opl_backprop = Backpropagation.output_layer_backpropagate(opl, output, lab, o_b, LEARNING_RATE)
        hl_b_backprop = Backpropagation.hidden_layer_backpropagate(hl_b, o_a, o_b, opl_backprop, LEARNING_RATE)
        hl_a_backprop = Backpropagation.hidden_layer_backpropagate(hl_a, img, o_a, hl_b_backprop, LEARNING_RATE)
    
        """ if j % 1000 == 0:
            print("    " + str(j))
        j += 1 """
    
    """ print("----")
    for n in hl_a.neurons:
        print(n.weights)
    print("----")
    for n in hl_b.neurons:
        print(n.weights)
    print("----")
    for n in opl.neurons:
        print(n.weights) """

    print("Iteration " + str(iter) + " done! Now testing accuracy...")

    right_amount = 0
    for (img_t, lab_t) in zip(test_images_flat, test_labels):
        oa = hl_a.generate_output(img_t)
        ob = hl_b.generate_output(oa)
        op = opl.generate_output(ob)
        pred = Utils.make_prediction(op)
        """ print("----")
        print(oa)
        print(ob)
        print(op)
        print(pred)
        print(lab_t) """
        if pred == lab_t:
            right_amount += 1
    
    print("Correct predictions: " + str(right_amount))

    """ if (iter >= ITERATION_CAP):
        break """
    
    if (prev_correct >= ACCURACY_CAP):
        break

    #if (prev_correct > right_amount):
    #    break

    prev_correct = right_amount
    iter = iter + 1

IO.save_layer(hl_a, "test3_a")
IO.save_layer(hl_b, "test3_b")
IO.save_layer(opl, "test3_c")