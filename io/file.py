path = 'D:\\PycharmProjects\\study-python\\exception\\try.py'

f = open(path, 'r')

content = f.read()

print(content)

try:
    f2 = open(path, 'r')
    print(f2.read())
finally:
    if f2:
        f2.close()

with open(path, 'r') as f3:
    print(f3.read())

with open(path, 'r') as f4:
    for line in f4.readlines():
        print(line.strip())

with open("C:\\Users\\frosoft2\\Pictures\\20170901144910.png", 'rb') as f5:
    print(f5.read().__len__())

with open("C:\\Users\\frosoft2\\Pictures\\text.txt", 'w') as f6:
    f6.write("Hello f6.")

with open("C:\\Users\\frosoft2\\Pictures\\text.txt", 'r') as f7:
    content = f7.read()
    print(content)
    assert "Hello f6." == content
