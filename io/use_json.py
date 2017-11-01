import json

d = dict(name='Bob', age=18, score=88)
print(d)

print(json.dumps(d))

print(json.loads(json.dumps(d)))
