class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('xty')
print(s)

s()

print(callable(Student("xty")))
print(callable(s))


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for n in range(stop):
                if n >= start:
                    L.append(a)
                a, b = b, a + b
            return L


for n in Fib():
    print(n)

fib = Fib()
print(fib[0])
print(fib[3])
print(fib[5])

print(fib[:5])
