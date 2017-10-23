age = 20

if age > 18:
    print("you age is ", age)
    print("adult")
else:
    print("teenager")

# out put is "5"
if age > 5:
    print("5")
elif age > 10:
    print("10")
else:
    print(age)

# str to int 
birth = input("birth:")
birth = int(birth)
if birth < 2000:
    print("00前")
else:
    print("00后")
