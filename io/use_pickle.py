import pickle
import os

d = dict(name='Bob', age=18, score=88)

print(pickle.dumps(d))

f = open("dump.txt", 'wb')

pickle.dump(d, f)

f.close()

with open("dump.txt", "rb") as f:
    d2 = pickle.load(f)
    print(d2)

os.remove("dump.txt")
