import re

data = [
    "Hello World!",
    "Hi pythonistas.",
    "Hello phpists and bye",
    "HELLO AND GOODBYE.",
    "Abracadabra",
    "import antigravity"]

# 1. Solution
res = 0
ind = 0
for i, s in enumerate(data):
    tmp = s.lower().count('a')
    if tmp > res:
        res = tmp
        ind = i
print "1. The string with max 'a' is " + "'" + data[ind] + "'"

# 2. Solution
print "\n2. The odd strings are: " + str(data[::2])[1:-1]

# 3. Solution
aim = data[0].lower().count(
    'hello', 0, 5) and not data[0].lower().count('bye', -3)

print '\n3. The strings with "hello" but NOT with "bye" are:'
aim = False
for s in data:
    aim = s.lower().count('hello', 0, 5) and not s.lower().count('bye', -3)
    if aim:
        print "\t" + s

# 4. Solution
print '\n4. ' + ' '.join(sorted(data))
