import unittest
from Vector import Vector

class TestVector(unittest.TestCase):
    def setUp(self):
        self.vec_a = Vector([1, 2, 3])
        self.vec_b = Vector([0, -10, 1.5])
        self.vec_c = Vector([0, 0, 0, 0])
    
    def test_str(self):
        self.assertEqual(str(self.vec_a), "[1, 2, 3]")

    def test_getitem(self):
        self.assertEqual(self.vec_a[1], 2)
    
    def test_len(self):
        self.assertEqual(len(self.vec_a), 3)
    
    def test_add(self):
        self.assertEqual(self.vec_a + self.vec_b, Vector([1, -8, 4.5]))
    
    def test_sub(self):
        self.assertEqual(self.vec_a - self.vec_b, Vector([1, 12, 1.5]))

    def test_sum(self):
        self.assertEqual(sum(self.vec_a), 6)
        self.assertEqual(sum(self.vec_b), -8.5)
    
    def test_mul_vec(self):
        self.assertEqual(self.vec_a * self.vec_b, -15.5)
    
    def test_mul_int(self):
        self.assertEqual(self.vec_b * -2, Vector([0, 20, -3]))