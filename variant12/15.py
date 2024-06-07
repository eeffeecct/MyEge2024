def f(a):
    for x in range(1, 100):
        if ((x % 12 == 0) and (70 <= x <= 80) and (x % a != 0)) == True:
            return False
    return True
            
for a in range(1, 100): 
    if f(a):
        print(a)