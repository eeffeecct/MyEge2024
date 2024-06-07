def f(x,y,p):
    if x + y >= 135 or p > 4:
        return p == 2 or p == 4
    if p % 2:
        return f(x+5,y,p+1) or f(x*3,y,p+1) or f(x,y+5,p+1) or f(x,y*3,p+1)
    else :
        return f(x+5,y,p+1) and f(x*3,y,p+1) and f(x,y+5,p+1) and f(x,y*3,p+1)

print(([i for i in range(1,122) if f(13,i,0)]))