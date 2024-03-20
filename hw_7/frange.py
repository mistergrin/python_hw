class Frange:

    def __init__(self, start, stop=None, step=1.0):
        if stop == None:
            stop = start
            start = 0
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.current >= self.stop and self.step > 0) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        result = self.current
        self.current += self.step
        return result


assert list(Frange(5)) == [0, 1, 2, 3, 4]
assert list(Frange(10, 2, step=-2)) == [10, 8, 6, 4]
assert list(Frange(10, 2, -2)) == [10, 8, 6, 4]
assert(list(Frange(2, 5)) == [2, 3, 4])
assert(list(Frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(Frange(1, 5)) == [1, 2, 3, 4])
assert(list(Frange(100, 0)) == [])
assert(list(Frange(5)) == [0, 1, 2, 3, 4])
assert(list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5])
for i in Frange(10, 2, -2):
    print(i)