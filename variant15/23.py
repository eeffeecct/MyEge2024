def f(x, y):
    if x == y:
        return 1
    elif x > y or 10 <= x <= 19:
        return 0
    else: 
        return f(x+1,y) + f(x+11,y) + f(x+8,y) + f(x*3,y)
    
print(f(2,27) * f(27, 33) * f(33, 50))
