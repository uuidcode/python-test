from unittest import TestCase
from point import *

class TestPoint(TestCase):
    def test(self):
        p = Point(3, 4)
        self.assertEqual(p.distance(), 5)