def f(x, y):
    if x == y:
        return 1
    elif x < y:
        return 0
    else:
        return f(x - int(str(x**2)[0]), y) + f(x - sum([int(x) for x in str(x)]), y)


print(f(32, 1))