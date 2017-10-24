print(list(map(lambda x: x * x, list(range(10)))))


def build(x, y):
    return lambda: x * x + y * y


print(build(1, 2))

print(build(1, 2)())
