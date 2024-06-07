def f(x, y, p):
    if x == y and p[-3:] == 'bab': 
        return 1
    elif x > y: 
        return 0
    else: 
        return f(x+1,y,p+'a') + f(x*2,y,p+'b') + f(x+5,y,p+'c')

print(f(5, 62, ''))




