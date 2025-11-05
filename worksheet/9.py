class Countdown:

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.i = self.num + 1
        while self.i > 1:
            self.i -= 1
            yield self.i
        return self


class SquareIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.i = 0
        while self.i < self.n:
            self.i += 1
            yield self.i**2
        return self


def fibonacci(n):
    a, b = 0, 1
    for _ in range(0, n):
        yield a
        a, b = b, b + a


for num in Countdown(5):
    print(num)

for s in SquareIterator(5):
    print(s)

for num in fibonacci(10):
    print(num)
