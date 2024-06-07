def f(x, y, k): 
    if x > y : 
        return 0
    if x == y and k == 1: 
        return 1
    else: 
        return f(x+1,y,k) + f(x+2,y,k) + f(x*2,y,k+1) + f(x*3,y,k+1) 
    
print(f(1,11,0))
