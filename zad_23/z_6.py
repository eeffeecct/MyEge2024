def f(x, y):
    if x == y:
        return 1
    elif x < y:
        return 0
    else:
        return f(x-3, y) + f(x // 7, y)


print(f(50, 1))

# otvet: 6
