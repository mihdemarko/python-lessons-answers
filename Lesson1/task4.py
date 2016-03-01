d = {"q": 3, "w": 8, "e": "z", "r": "5", "t": 3}

# 1. Solution
answ = dict((value, key) for key, value in d.iteritems())
print '1. The switched key-values are: ' + str(answ)

# 2. Solution
print '\n2. The values sorted by key:',
for key in sorted(d):
    print d[key],

# 3. Solution
for key, value in d.iteritems():
    if 'int' in str(type(value)):
        d[key] = value + 1
    else:
        d[key] = value + 'b'
print '\n\n3. ' + str(d)
