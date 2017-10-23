import os

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in "ABC" for n in "XYZ"])

print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}

print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']

print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]

print([v for v in L1 if isinstance(v, str)])
