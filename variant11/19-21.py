def f(x, p):
    if x == 0 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f(x - 5, p + 1) or f(x // 3, p + 1) 
    else: 
        return f(x - 5, p + 1) and f(x // 3, p + 1) 
    

print(([x for x in range(100, 1, -1) if f(x, 0)]))