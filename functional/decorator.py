import functools


def now():
    print('2017-10-24')


f = now

f()

print(now.__name__)
print(f.__name__)


def log(func):
    def wrapper(*args, **kwargs):
        print("call %s():" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def log_now():
    print('2017-10-24')


log_now()


def log2(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("%s %s" % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log2('execute')
def log2_now():
    print('2017-10-24')


log2_now()

print(log2_now.__name__)


def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("call %s():" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log3
def log3_now():
    print('2017-10-24')


log3_now()

print(log3_now.__name__)


def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s %s" % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log4('execute')
def log4_now():
    print('2017-10-24')


log4_now()

print(log4_now.__name__)


def log5(text='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s %s" % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log5('execute')
def log5_now():
    print('2017-10-24')


log5_now()

print(log5_now.__name__)


@log5
def log6_now():
    print('2017-10-24')


log6_now()

print(log6_now.__name__)
