def f19(x,y,p):
    if x + y >= 189 or p > 2:
        return p == 2
    if p % 2:
        if x < y:
            return f19(x*y, y, p + 1) or f19(x, y*x, p + 1) or f19(y, y, p+1)
        elif y <= x:
            return f19(x*y, y, p + 1) or f19(x, y*x, p + 1) or f19(x, x, p+1)
    else:
        if x <= y:
            return f19(x*y, y, p + 1) and f19(x, y*x, p + 1) and f19(y, y, p+1)
        elif y <= x:
            return f19(x*y, y, p + 1) and f19(x, y*x, p + 1) and f19(x, x, p+1)


def f20(x,y,p):
    if x + y >= 189 or p > 3:
        return p == 3
    if p % 2 == 0:
        if x < y:
            return f20(x*y, y, p + 1) or f20(x, y*x, p + 1) or f20(y, y, p+1)
        elif y < x:
            return f20(x*y, y, p + 1) or f20(x, y*x, p + 1) or f20(x, x, p+1)
    else:
        if x < y:
            return f20(x*y, y, p + 1) and f20(x, y*x, p + 1) and f20(y, y, p+1)
        elif y < x:
            return f20(x*y, y, p + 1) and f20(x, y*x, p + 1) and f20(x, x, p+1)


def f21(x,y,p):
    if x + y >= 189 or p > 4:
        return p == 2 or p == 4
    if p % 2:
        if x < y:
            return f21(x*y, y, p + 1) or f21(x, y*x, p + 1) or f21(y, y, p+1)
        elif y <= x:
            return f21(x*y, y, p + 1) or f21(x, y*x, p + 1) or f21(x, x, p+1)
    else:
        if x < y:
            return f21(x*y, y, p + 1) and f21(x, y*x, p + 1) and f21(y, y, p+1)
        elif y < x:
            return f21(x*y, y, p + 1) and f21(x, y*x, p + 1) and f21(x, x, p+1)
















print(([i for i in range(1,184) if f19(5, i, 0)]))
print(([i for i in range(1,184) if f20(5, i, 0)]))
print(([i for i in range(1,184) if f21(5, i, 0)]))
