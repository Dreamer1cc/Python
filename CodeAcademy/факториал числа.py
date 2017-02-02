def factorial(x):
    if x == 1:
        return x
    elif x == 0:
        return 1
    else:
        for n in range(x):
            n = x * factorial(x-1)
    return n


factorial(5)
