class Student(object):
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be integer.")
        if score < 0 or score > 100:
            raise ValueError("score must between 0 ~100!")
        self.__score = score


s = Student()

s.set_score(100)

print(s.get_score())


class Student2(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be integer.")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~100!")
        self._score = value


s2 = Student2()

s2.score = 100

print(s2.score)


class Student3(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth


s3 = Student3()

s3.birth = 2016

print(s3.age)


class Screen(object):
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        self._width = width

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height


screen = Screen()

screen.width = 1024
screen.height = 768
print(screen.resolution)

assert screen.resolution == 786432, '1024 * 768 = %d ?' % screen.resolution
