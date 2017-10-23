normalList = [1, 2, 3, 5, 6]

print(normalList[0:3])
print(normalList[:3])
print(normalList[1:3])
print(normalList[-2])
print(normalList[-2:-1])

rangeList = list(range(100))

# before ten element
print(rangeList[:10])

# after ten element
print(rangeList[-10:])

# between 10 - 20
print(rangeList[10:20])

# before ten element per 2
print(rangeList[:10:2])

# all data per five 
print(rangeList[::5])

# copy list
print(rangeList[:])

normalTuple = (1, 2, 3, 4, 5)

print(normalTuple[:3])

# string slice
print("ABCDEFG"[:3])
