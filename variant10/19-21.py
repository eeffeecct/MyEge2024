# def f(x,y,p):
#     if (x**2+y**2)**0.5 >= 13 or p > 2:
#         return p == 2
    
#     return f(x+3,y,p+1) or f(x,y+3,p+1) or f(x,y+4,p+1)
    
# print(([i for i in range(1, 13) if f(i, 2, 0)]))

# def f(x,y,p):
#     if (x**2+y**2)**0.5 >= 13 or p > 3:
#          return p == 3
#     if p % 2 == 0:
#         return f(x+3,y,p+1) or f(x,y+3,p+1) or f(x,y+4,p+1)
#     else:
#         return f(x+3,y,p+1) and f(x,y+3,p+1) and f(x,y+4,p+1)

# print(([i for i in range(1, 13) if f(i, 2, 0)]))

def f(x,y,p):
    if (x**2+y**2)**0.5 >= 13 or p > 4:
         return p == 2 or p == 4
    if p % 2:
        return f(x+3,y,p+1) or f(x,y+3,p+1) or f(x,y+4,p+1)
    else:
        return f(x+3,y,p+1) and f(x,y+3,p+1) and f(x,y+4,p+1)

print(([i for i in range(1, 13) if f(i, 2, 0)]))
