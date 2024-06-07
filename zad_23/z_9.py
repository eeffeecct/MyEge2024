def f(x, y, p):
    if x == y:
        return 1
    elif x > y:
        return 0
    else:
        if p == 0:
            return f(x + 1, y, 1) + f(x + 3, y, 0) + f(x * 2, y, 0)
        else:
            return f(x + 3, y, 0) + f(x * 2, y, 0)


print(f(3, 30, 0))

# otvet: 407
