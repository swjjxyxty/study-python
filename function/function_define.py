def my_abs(value):
    if value >= 0:
        return value
    else:
        return -value


print(my_abs(-100))


# empty function

def nop():
    pass


# type check

def my_abs_with_type_check(value):
    if not isinstance(value, (int, float)):
        raise TypeError('bad operand type')
    if value >= 0:
        return value
    else:
        return -value


# print(my_abs_with_type_check('100'))
print(my_abs_with_type_check(-100))


# return multi value , actual return value is a tuple.
def move(x, y):
    return x, y


x, y = move(1, 2)
print(x, y)
