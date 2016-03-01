input = [1, 2, 3, 4, [4, 5, [6, 7]], 8]
output = []

isLst = lambda x: 'list' in str(type(x))


def unpack(lst):
    for item in lst:
        if isLst(item):
            unpack(item)
        else:
            output.append(item)
unpack(input)

print output
