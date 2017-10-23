d = {'m': 99, 'k': 20, "j": 10}

print(d['m'])

# put new element
d['n'] = 100

print(d['n'])

# check key exist
print('n' in d)
print('o' in d)

# get
print(d.get('n'))
# get with default value
print(d.get('0', -1))

# delete

d.pop('n')
print('n' in d)
