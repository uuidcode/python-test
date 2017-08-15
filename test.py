import math
import unittest
from mylib import *

a = 1
b = 2
c = a + b

n = math.sqrt(9)

def sum(a, b):
    return a + b

class Test(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(c, 3)

    def testSum(self):
        self.assertEqual(sum(1, 2), 3)

    def testSubtract(self):
        self.assertEqual(substract(2, 1), 1)
