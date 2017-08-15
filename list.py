from unittest import TestCase

class TestList(TestCase):
    def test(self):
        a = [1, 2, 3]
        b = [2, 3, 4]
        c = a + b
        self.assertEqual(len(c), 6)