# def f1(x, y, p):
#     if x >= 52 or p > 2: 
#         return p == 2    
#     return f1(x+1,p+1) or f1(x+10,p+1) 
    
    
def f2(x, y, p):
    if x + y >= 59 or p > 3: 
        return p == 3
    if p % 2 == 0: 
        return f2(x+1,y,p+1) or f2(x*2,y,p+1) or f2(x,y+1,p+1) or f2(x,y*2,p+1) 
    else: 
        return f2(x+1,y,p+1) and f2(x*2,y,p+1) and f2(x,y+1,p+1) and f2(x,y*2,p+1) 

def f3(x, y, p):
    if x + y >= 59 or p > 4:
        return p == 2 or p == 4
    if p % 2: 
        return f3(x+1,y,p+1) or f3(x*2,y,p+1) or f3(x,y+1,p+1) or f3(x,y*2,p+1) 
    else: 
        return f3(x+1,y,p+1) and f3(x*2,y,p+1) and f3(x,y+1,p+1) and f3(x,y*2,p+1) 
    

# print(([i for i in range(1, 52) if f1(i, 0)]))
print(([i for i in range(1, 53) if f2(5, i, 0)]))
print(([i for i in range(1, 53) if f3(5, i, 0)]))

