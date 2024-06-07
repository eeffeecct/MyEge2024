def f(x, p):
    if x >= 55 or p > 4: 
        return p == 2 or p == 4
    if p % 2: 
        return f(x+1,p+1) or f(x+4,p+1) or f(x*3,p+1)
    else:
        return f(x+1,p+1) and f(x+4,p+1) and f(x*3,p+1)

print(([x for x in range(1, 55) if f(x, 0)]))