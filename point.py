import math

class Point:
    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.count += 1

    def distance(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def getCount():
        return Point.count