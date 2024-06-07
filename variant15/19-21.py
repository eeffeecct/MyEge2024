def f(x,p):
    if x >= 649 or p > 4: 
        return p == 2 or p == 4
    if p % 2: 
        return f(x+7,p+1) or f(x+13,p+1) or f(x*11,p+1)
    else: 
        return f(x+7,p+1) and f(x+13,p+1) and f(x*11,p+1)

print(([i for i in range(1, 64) if f(i, 0)]))