class Student(object):
    pass


bart = Student()

print(bart)

bart.name = "xty"
print(bart.name)


class Student2(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_self(self):
        print('%s: %s' % (self.__name, self.__score))


bart = Student2("name", 100)

bart.print_self()

