import types

print(type(123))
print(type(str))

print(type('str'))

print(type(abs))

print(type(123) == type(456))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(isinstance(abs, types.BuiltinFunctionType))
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

print(dir('ABC'))

print('ABC'.__len__())


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, "x"))
print(hasattr(obj, "y"))

setattr(obj, 'x', 19)
print(obj.x)

print(getattr(obj, "x"))
print(getattr(obj, "y", -1))
