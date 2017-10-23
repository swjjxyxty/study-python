normalTuple = ('1', "2", "3")
# tuple is unmodifiable
print(normalTuple)

print(normalTuple[0])

print(len(normalTuple))

print(normalTuple[-1])

emptyTuple = ()
print(emptyTuple)
print(len(emptyTuple))

singleTuple = (1,)
print(singleTuple)
print(len(singleTuple))

changeableTuple = (1, 2, [1, 2])
print(changeableTuple)

changeableTuple[2][0] = 3
print(changeableTuple)
