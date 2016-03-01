def isSimple(n):
    res = True
    for i in range(2, abs(n)):
        if n % i == 0:
            res = False
            break
    return res


def allSimples(n):
    for i in range(2, n+1):
        if isSimple(i):
            yield i

print "The simple numbers in 500 are: " + str([i for i in allSimples(500)])[1:-1]
