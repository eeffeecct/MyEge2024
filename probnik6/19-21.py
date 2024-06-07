def f(x,y,p):
    if x + y >= 157 or p > 4:
        return p == 2 or p == 4
    if p % 2:
        return f(x+1,y,p+1) or f(x+2,y,p+1) or f(x,y+1,p+1) or f(x,y+2,p+1) or f(x*3,y,p+1) or f(x,y*3,p+1)
    else: 
        return f(x+1,y,p+1) and f(x+2,y,p+1) and f(x,y+1,p+1) and f(x,y+2,p+1) and f(x*3,y,p+1) and f(x,y*3,p+1)
    
print(([i for i in range(1, 140) if f(17,i,0)]))