from types import MethodType


class Student(object):
    pass


s = Student()
# bind property
s.name = 'xty'

print(s.name)


def set_age(self, age):
    self.age = age


# bind method for instance
s.set_age = MethodType(set_age, s)

s.set_age(25)

print(s.age)


def set_score(self, score):
    self.score = score


# bind method for class
Student.set_score = set_score

s.set_score(90)

print(s.score)


# limit bind proerty

class Student2(object):
    __slots__ = ('names', 'age')


s2 = Student2()

s2.names = "xty"

s2.age = 25


# will be failed
# s2.score = 30


class GraduateStudent(Student2):
    pass


gs = GraduateStudent()

gs.score = 30

print(gs.score)
