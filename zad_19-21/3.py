def f19(x, p):
    if x >= 40 or p > 2:
        return p == 2
    if p % 2:   # нечет
        return f19(x + 1, p + 1) or f19(x * 3 - 2, p + 1)
    else:
        return f19(x + 1, p + 1) and f19(x * 3 - 2, p + 1)


def f20(x, p):
    if x >= 40 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f20(x + 1, p + 1) or f20(x * 3 - 2, p + 1)
    else:
        return f20(x + 1, p + 1) and f20(x * 3 - 2, p + 1)


def f21(x, p):
    if x >= 40 or p > 4:
        return p == 2 or p == 4
    if p % 2:
        return f21(x + 1, p + 1) or f21(x * 3 - 2, p + 1)
    else:
        return f21(x + 1, p + 1) and f21(x * 3 - 2, p + 1)


print(([i for i in range(1, 40) if f19(i, 0)]))     # 13
print(([i for i in range(1, 40) if f20(i, 0)]))     # 5 12
print(([i for i in range(1, 40) if f21(i, 0)]))     # 11
