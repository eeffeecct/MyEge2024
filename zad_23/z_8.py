def f(x, y):
    if x == y:
        return 1
    elif x < y:
        return 0
    else:
        return f(x - 2, y) + f(x - 3, y) + f(x ** 0.5, y)


print(f(25, 3))

# otvet: 238
