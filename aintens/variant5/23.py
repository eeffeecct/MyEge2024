def f(x, y):
    if x > y or x == 16:
        return 0
    if x == y: 
        return 1
    else: 
        return f(x+1,y) + f(x+3,y) + f(x**2,y)

print(f(3,20)*f(20,26))