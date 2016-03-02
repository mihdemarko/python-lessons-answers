def argSumm(a, b, *args, **kwargs):
    """Returns the sum of its arguments
    """
    return a + b + sum(args) + sum(kwargs.values())

print 'The sum of function arguments is: ' + str(argSumm(3, 4, 5, num=4))
