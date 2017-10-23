# generator
g = (x * x for x in range(1, 11))
# get next value
print(next(g))

for i in g:
    print(i)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print(next(fib(5)))

for n in fib(6):
    print(n)
