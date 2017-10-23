s = {1, 2, 3}
print(s)

# can't save same value
s = {1, 1, 2, 3, 4, 4}
print(s)

# add element
s.add(5)
print(s)

# remove element
s.remove(5)
print(s)

s1 = {1, 2, 3, 4}
s2 = {1, 5, 6, 7, 8}

print(s1 & s2)
print(s1 | s2)
