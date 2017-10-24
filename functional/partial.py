import functools

print(int('12345'))

print(int('12345', base=8))


def int2(s, base=2):
    return int(s, base)


print(int2('1000000'))

int8 = functools.partial(int, base=8)

print(int8('12345'))

max2 = functools.partial(max, 10)

print(max2(1, 2, 3, 4))
