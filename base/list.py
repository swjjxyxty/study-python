normalList = ['1', '2', '3']

print(normalList)

# calculate list size
print(len(normalList))

# access list element ,index start from 0, end with len-1
print(normalList[0])

print(normalList[len(normalList) - 1])

# access last element
print(normalList[-1])

# append element
normalList.append("4")
print(normalList)

# insert element
normalList.insert(1, "5")
print(normalList)

# delete last element
normalList.pop()
print(normalList)

# delete special index element
normalList.pop(1)
print(normalList)

# replace element
normalList[1] = "5"
print(normalList)

# any type in list

normalList[2] = ["7", "8"]
print(normalList)
# get "7"
print(normalList[2][0])

# empty list
emptyList = []
print(len(emptyList))
