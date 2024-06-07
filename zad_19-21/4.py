def f19(x, y, p):
    if x + y >= 47 or p > 2:
        return p == 2
    if p % 2:   # нечет
        return f19(x + 1, y + 2, p + 1) or f19(x + 2, y + 1, p + 1) or f19(x * 2, y, p + 1) or f19(x, y * 2, p + 1)
    else:
        return f19(x + 1, y + 2, p + 1) and f19(x + 2, y + 1, p + 1) and f19(x * 2, y, p + 1) and f19(x, y * 2, p + 1)


def f20(x, y, p):
    if x + y >= 47 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f20(x + 1, y + 2, p + 1) or f20(x + 2, y + 1, p + 1) or f20(x * 2, y, p + 1) or f20(x, y * 2, p + 1)
    else:
        return f20(x + 1, y + 2, p + 1) and f20(x + 2, y + 1, p + 1) and f20(x * 2, y, p + 1) and f20(x, y * 2, p + 1)


def f21(x, y, p):
    if x + y >= 47 or p > 4:
        return p == 2 or p == 4
    if p % 2:
        return f21(x + 1, y + 2, p + 1) or f21(x + 2, y + 1, p + 1) or f21(x * 2, y, p + 1) or f21(x, y * 2, p + 1)
    else:
        return f21(x + 1, y + 2, p + 1) and f21(x + 2, y + 1, p + 1) and f21(x * 2, y, p + 1) and f21(x, y * 2, p + 1)


print(([i for i in range(1, 37) if f19(10, i, 0)]))     # 17

print(([i for i in range(1, 37) if f20(10, i, 0)]))     # 16

print(([i for i in range(1, 37) if f21(10, i, 0)]))     # 12
