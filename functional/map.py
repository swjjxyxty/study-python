def f(x):
    return x * x


normalList = list(range(10))
print(list(map(f, normalList)))
print(list(map(str, normalList)))
