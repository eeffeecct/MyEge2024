def f21(x, p):
    if x >= 72 or p > 4:
        return p == 2 or p == 4
    if p % 2:
        return f21(x+3,p+1) or f21(x+5,p+1) or f21(x*2,p+1)
    else:
        return f21(x+3,p+1) and f21(x+5,p+1) and f21(x*2,p+1)

print(([i for i in range(1, 72) if f21(i, 0)])) 
