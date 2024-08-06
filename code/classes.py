class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(12, 13)
another_point = Point(23, 12)

print(another_point + point)

"""
TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
"""