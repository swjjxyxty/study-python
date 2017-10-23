# position parameter

def power(x):
    return x * x


print(power(5))


# default parameter

def power_with_default_parameter(x, n=5):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print(power_with_default_parameter(5))
print(power_with_default_parameter(5, 2))


# changeable parameter
def calc(*numbers):
    result = 0
    for number in numbers:
        result = result + number * number
    return result


print(calc(1, 2, 3))
print(calc(1, 2, 3, 4, 5))

nums = [1, 2, 3, 4]
print(calc(nums[0], nums[1]))

print(calc(*nums))


# keywords parameter

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('xty', 10)
person('xty', 10, city='GZ', home='HN')

extra = {'city': 'GZ', 'home': 'HN'}
person('xty', 10, **extra)


# named keywords parameter

def person(name, age, *, city, job):
    print(name, age, city, job)


person("xty", 11, city='GZ', job='HN')


def person(name, age, *args, city, job):
    print(name, age, args, city, job)


person("xty", 11, {1, 2, 3}, city='GZ', job='HN')


def person(name, age, *, city='GZ', job):
    print(name, age, city, job)


person("xty", 11, job='HN')


# composite parameter
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
