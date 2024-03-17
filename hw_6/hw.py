from class_hw import Circle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


b = Point(x=3, y=6)
o1 = Circle(x=4, y=5, radius=2)

print(b in o1)
