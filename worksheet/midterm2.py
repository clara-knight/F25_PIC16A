import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = self.compute_area()
        self.circumference = self.compute_circumference()

    def compute_area(self):
        return math.pi * (self.radius**2)

    def compute_circumference(self):
        return 2 * math.pi * self.radius


class Int:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.i = 0
        while self.i < self.n:
            self.i += 1
            yield self.i


circle = Circle(6)
print(circle.radius, circle.area, circle.circumference)

a = Int(10)
for i in a:
    print(i)
