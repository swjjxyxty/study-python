# -*_ coding:utf-8 -*-

names = ["1", "2", "3"]

for name in names:
    print(name)

sum = 0

for x in range(101):
    sum += x
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

n = 1
while n < 1000:
    if n > 10:
        break
    print(n)
    n = n + 1
print("END")

n = 1
while n < 1000:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
print("END")
