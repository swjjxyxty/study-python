def calc_sum(*args):
    ax = 0
    for a in args:
        ax = ax + a
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 3, 4, 5)
print(f)

print(f())

f2 = lazy_sum(1, 2, 3, 4, 5)

print(f == f2)
