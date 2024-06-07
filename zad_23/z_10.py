def f(x, y, k=0):
    if x % 6 != 0:
        k += 1
    if x == y:
        return 1
    if x > y or k == 4:
        return 0
    else:
        return f(x + 2, y) + f(x * 2, y) + f(x * 3, y)


print(f(1, 300))

# otvet: 358874
