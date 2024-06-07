def f(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    else:
        if (x+1) % 3 == 0:
            return f(x + 1, y) + f(int(str(x) + '1'), y) + f(x * 5, y)
        else:
            return f(x + 1, y) + f(x * 5, y)


def plus(a):
    if a % 3 == 0:
        return str(a) + '1'
    else:
        return a


print(f(1, 410))

# otvet: 1440
