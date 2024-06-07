def f19(x, y, p):
    if x + y >= 231 or p > 2:
        return p == 2
    return f19(x * 2, y, p + 1) or f19(x + 1, y, p + 1) or f19(x, y * 2, p + 1) or f19(x, y + 1, p + 1)



def f20(x, y, p):
    if x + y >= 231 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f20(x * 2, y, p + 1) or f20(x + 1, y, p + 1) or f20(x, y * 2, p + 1) or f20(x, y + 1, p + 1)
    else:
        return f20(x * 2, y, p + 1) and f20(x + 1, y, p + 1) and f20(x, y * 2, p + 1) and f20(x, y + 1, p + 1)


def f21(x, y, p):
    if x + y >= 231 or p > 4:
        return p == 2 or p == 4
    if p % 2:
        return f21(x * 2, y, p + 1) or f21(x + 1, y, p + 1) or f21(x, y * 2, p + 1) or f21(x, y + 1, p + 1)
    else:
        return f21(x * 2, y, p + 1) and f21(x + 1, y, p + 1) and f21(x, y * 2, p + 1) and f21(x, y + 1, p + 1)


print(([i for i in range(1, 214) if f19(17, i, 0)]))
print(([i for i in range(1, 214) if f20(17, i, 0)]))
print(([i for i in range(1, 214) if f21(17, i, 0)]))
