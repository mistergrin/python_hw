class Circle:
    def __init__(self, x, y, radius):
        self.centre = (x, y)
        self.radius = radius

    def __contains__(self, point):
        return (point.x - self.centre[0])**2 + (point.y - self.centre[1])**2 <= self.radius ** 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


b = Point(x=3, y=6)
o1 = Circle(x=4, y=5, radius=1)

print(b in o1)
