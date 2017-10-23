from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for value in d.values():
    print(value)

for item in d.items():
    print(item)

for char in "ABC":
    print(char)

print(isinstance("ABC", Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate([1, 2, 3, 4, 5]):
    print(i, value)

for x, y in [(1, 1,), (2, 2), (3, 3)]:
    print(x, y)
