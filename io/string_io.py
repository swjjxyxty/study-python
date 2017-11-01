from io import StringIO

f = StringIO()

f.write("Hello")

f.write("Hi.")

f.write("bye bye.")

print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

for line in f.readlines():
    print(line.strip())
