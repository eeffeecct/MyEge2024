def f(x, y, p):
    if x + y >= 275 or p > 4:
        return p == 2 or p == 4
    if p % 2: 
        return f(x+3,y,p+1) or f(x+7,y,p+1) or f(x,y+3,p+1) or f(x,y+7,p+1) or f(x*4,y,p+1) or f(x,y*4,p+1)
    else: 
        return f(x+3,y,p+1) and f(x+7,y,p+1) and f(x,y+3,p+1) and f(x,y+7,p+1) and f(x*4,y,p+1) and f(x,y*4,p+1)
    
print(([i for i in range(1, 217) if f(58, i, 0)]))