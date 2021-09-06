import unittest
import Loss
import Utils
import Activation
import Backpropagation
from HiddenLayer import HiddenLayer
from Vector import Vector

class TestBackpropagation(unittest.TestCase):
    def setUp(self):
        self.inputs = Vector([5, 1])
        self.targets = [0.5]

        self.hl_a = HiddenLayer(2, 2, [[0.5, 1], [0.25, 0.25]], Activation.sigmoid, Activation.sigmoid_d, Loss.mean_quadratic, Loss.mean_quadratic_d, 0)
        self.hl_b = HiddenLayer(2, 2, [[0.1, 2], [0, 0.5]], Activation.sigmoid, Activation.sigmoid_d, Loss.mean_quadratic, Loss.mean_quadratic_d, 0.5)
        self.opl = HiddenLayer(1, 2, [[1, 0.5]], Activation.sigmoid, Activation.sigmoid_d, Loss.mean_quadratic, Loss.mean_quadratic_d, 0.25)

        self.op_a = self.hl_a.generate_output(self.inputs)
        self.op_b = self.hl_b.generate_output(self.op_a['op'])
        self.op = self.opl.generate_output(self.op_b['op'])
    
    def test_opl_backprop(self):

        self.op_prop = Backpropagation.output_layer_backpropagate(self.opl, self.op['op'], self.targets, self.op_b['op'], 0.5)

        self.assertEqual(round(Loss.mean_quadratic_d(self.targets[0], self.op['op'][0]), 2), 0.32)
        self.assertEqual(round(self.op['op'][0] * (1 - self.op['op'][0]), 2), 0.15)
        self.assertEqual(round(Loss.mean_quadratic_d(self.targets[0], self.op['op'][0]) * (self.op['op'][0] * (1 - self.op['op'][0])), 2), round(self.op_prop['tl'][0], 2))
        self.assertEqual(round(self.op_prop['tl'][0], 3), 0.047)
        for n in self.opl.neurons:
            for i in range(len(n.weights)):
                self.assertEqual(round(self.op_prop['w'][0][i] - self.op_b['op'][i] * self.op_prop['tl'][0] * 0.5, 3), round(n.weights[i], 3))