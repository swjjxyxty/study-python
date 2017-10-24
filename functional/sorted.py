normalList = [36, 5, -12, 9, -21]

print(sorted(normalList))

print(sorted(normalList, key=abs))

stringList = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(stringList))

print(sorted(stringList, key=str.lower))

print(sorted(stringList, key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)
