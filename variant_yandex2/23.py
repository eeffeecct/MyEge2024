def f(x, y):
    if x == y:
        return 1
    elif x > y or x == 25:
        return 0
    else:
        return f(x + 3, y) + f(x * 2, y) + f(x * 5, y)


print(f(5, 115))