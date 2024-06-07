def chet(a):
    if a % 2 == 0:
        return a // 2
    elif a % 2 != 0:
        return a // 2 + 1


def f19(x, y, p):
    if x + y <= 20 or p > 2:
        return p == 2
    if p % 2:
        return f19(x - 1, y, p + 1) or f19(chet(x), y, p + 1) or f19(x, y - 1, p + 1) or f19(x, chet(y), p + 1)
    else:
        return f19(x - 1, y, p + 1) and f19(chet(x), y, p + 1) and f19(x, y - 1, p + 1) and f19(x, chet(y), p + 1)


def f20(x, y, p):
    if x + y <= 20 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f20(x - 1, y, p + 1) or f20(chet(x), y, p + 1) or f20(x, y - 1, p + 1) or f20(x, chet(y), p + 1)
    else:
        return f20(x - 1, y, p + 1) and f20(chet(x), y, p + 1) and f20(x, y - 1, p + 1) and f20(x, chet(y), p + 1)


def f21(x, y, p):
    if x + y <= 20 or p > 4:
        return p == 2 or p == 4
    if p % 2:
        return f21(x - 1, y, p + 1) or f21(chet(x), y, p + 1) or f21(x, y - 1, p + 1) or f21(x, chet(y), p + 1)
    else:
        return f21(x - 1, y, p + 1) and f21(chet(x), y, p + 1) and f21(x, y - 1, p + 1) and f21(x, chet(y), p + 1)


print(([i for i in range(100, 10, -1) if f19(10, i, 0)]))     # 21
print(([i for i in range(100, 10, -1) if f20(10, i, 0)]))     # 22 42
print(([i for i in range(100, 10, -1) if f21(10, i, 0)]))     # 24
