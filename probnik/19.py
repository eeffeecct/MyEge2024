def f19(x, p):
    if p > 2 or x >= 195:
        if p == 2:
            return f19(x + 9, p + 1) or f19(x * 7, p + 1)
        else:
            return f19(x + 9, p + 1) and f19(x * 7, p + 1)



print(([i for i in range(1, 195) if f19(i, 0) ]))

