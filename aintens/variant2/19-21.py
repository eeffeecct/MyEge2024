def f(x, p): 
    if x >= 29 or p > 4: 
        return p == 2 or p == 4   
    if p % 2 : return f(x+1,p+1) or f(x+2,p+1) or f(x*3,p+1)
    else: return f(x+1,p+1) and f(x+2,p+1) and f(x*3,p+1)

print(([i for i in range(1, 29) if f(i,0)]))