from HiddenLayer import HiddenLayer
from Vector import Vector
import IO
import Loss
import Utils
import Activation
import Backpropagation
import Rate


# As a test, let's simulate the OR-gate with a single perceptron
""" training = []
training.append(Vector(2, arr=[1, 1]))
training.append(Vector(2, arr=[1, 0]))
training.append(Vector(2, arr=[0, 1]))
training.append(Vector(2, arr=[0, 0]))

labels = Vector(4, arr=[1, 1, 1, 0])
from Vector 
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

iter = 1eturn super().setUp()
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



# Final boss: a 32-16-10 multi-layer net!
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
    images_flat.append(Vector(Utils.normalize(Utils.flatten_2d(i), 0, 1)))
    labels_oh.append(Utils.onehot_label_arr(l))

for i in test_images:
    test_images_flat.append(Vector(Utils.normalize(Utils.flatten_2d(i), 0, 1)))

print("Images & labels processed!")

# Don't change these two
IMAGE_INPUT_SIZE = 784
OUTPUT_LAYER_SIZE = 10

# These define how many neurons in layers A & B
LAYER_A_SIZE = 32
LAYER_B_SIZE = 16

# Initialize weights and layer
weights_a = [Utils.rand_array(IMAGE_INPUT_SIZE, -1, 1) for _ in range(LAYER_A_SIZE)]
weights_b = [Utils.rand_array(LAYER_A_SIZE, -1, 1) for _ in range(LAYER_B_SIZE)]
weights_op = [Utils.rand_array(LAYER_B_SIZE, -1, 1) for _ in range(OUTPUT_LAYER_SIZE)]

hl_a = HiddenLayer(LAYER_A_SIZE, IMAGE_INPUT_SIZE, weights_a,  Activation.sigmoid, Activation.sigmoid_d, Loss.mean_quadratic, Loss.mean_quadratic_d, 0)
hl_b = HiddenLayer(LAYER_B_SIZE, LAYER_A_SIZE, weights_b,  Activation.sigmoid, Activation.sigmoid_d, Loss.mean_quadratic, Loss.mean_quadratic_d, 0)
opl = HiddenLayer(OUTPUT_LAYER_SIZE, LAYER_B_SIZE, weights_op,  Activation.sigmoid, Activation.sigmoid_d, Loss.quadratic, Loss.quadratic_d, 0)

ITERATION_CAP = 20
ACCURACY_CAP = 9800

LEARNING_DECAY_SCALAR = 0.0025
BATCH_SIZE = 100

learning_rate = 0.05
iter = 1
prev_correct = 0

while True:
    print("Iteration: " + str(iter))

    learning_rate = Rate.decaying(learning_rate, iter, LEARNING_DECAY_SCALAR)

    print("Learning rate: " + str(learning_rate))
    
    j = 1
    batchtracker = 0
    img_sum = Vector([0] * IMAGE_INPUT_SIZE)
    lab_sum = Vector([0] * OUTPUT_LAYER_SIZE)
    oa_sum = Vector([0] * LAYER_A_SIZE)
    ob_sum = Vector([0] * LAYER_B_SIZE)
    op_sum = Vector([0] * OUTPUT_LAYER_SIZE)

    for (img, lab) in zip(images_flat, labels_oh):
        o_a = hl_a.generate_output(img)
        o_b = hl_b.generate_output(o_a['op'])
        output = opl.generate_output(o_b['op'])

        img_sum = img_sum + img
        lab_sum = lab_sum + Vector(lab)
        oa_sum = oa_sum + o_a['op']
        ob_sum = ob_sum + o_b['op']
        op_sum = op_sum + output['op']

        batchtracker = batchtracker + 1

        if batchtracker == BATCH_SIZE:
            img_sum = img_sum * (1 / BATCH_SIZE)
            lab_sum = lab_sum * (1 / BATCH_SIZE)
            oa_sum = oa_sum * (1 / BATCH_SIZE)
            ob_sum = ob_sum * (1 / BATCH_SIZE)
            op_sum = op_sum * (1 / BATCH_SIZE)

            #print(opl.loss(lab_sum, op_sum))

            opl_backprop = Backpropagation.output_layer_backpropagate(opl, op_sum, lab, ob_sum, learning_rate)
            hl_b_backprop = Backpropagation.hidden_layer_backpropagate(hl_b, oa_sum, ob_sum, opl_backprop, learning_rate)
            hl_a_backprop = Backpropagation.hidden_layer_backpropagate(hl_a, img, oa_sum, hl_b_backprop, learning_rate)

            img_sum = Vector([0] * IMAGE_INPUT_SIZE)
            lab_sum = Vector([0] * OUTPUT_LAYER_SIZE)
            oa_sum = Vector([0] * LAYER_A_SIZE)
            ob_sum = Vector([0] * LAYER_B_SIZE)
            op_sum = Vector([0] * OUTPUT_LAYER_SIZE)
            batchtracker = 0

    
        if j % 10000 == 0:
            print("    " + str(j))
        j += 1

    print("Iteration " + str(iter) + " done! Now testing accuracy...")

    right_amount = 0
    for (img_t, lab_t) in zip(test_images_flat, test_labels):
        oa = hl_a.generate_output(img_t)['op']
        ob = hl_b.generate_output(oa)['op']
        op = opl.generate_output(ob)['op']
        pred = Utils.make_prediction(op)
        if pred == lab_t:
            right_amount += 1
    
    print("Correct predictions: " + str(right_amount))

    if (iter >= ITERATION_CAP):
        break
    
    if (prev_correct >= ACCURACY_CAP):
        break

    #if (prev_correct > right_amount):
    #    break

    prev_correct = right_amount
    iter = iter + 1

IO.save_layer(hl_a, "test3_a")
IO.save_layer(hl_b, "test3_b")
IO.save_layer(opl, "test3_c")