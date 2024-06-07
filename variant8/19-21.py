# def f(x, y, z, p):
#     if (x >= 20 or y >= 20 or z >= 20 or x+y+z >= 25) or p > 2:
#         return p == 2
#     if p % 2: 
#         return f(x*2,y,z,p+1) or f(x,y*2,z,p+1) or f(x,y,z*2,p+1) or f(x+2,y,z,p+1) or f(x,y+2,z,p+1) or f(x,y,z+2,p+1)
#     else:
#         return f(x*2,y,z,p+1) and f(x,y*2,z,p+1) and f(x,y,z*2,p+1) and f(x+2,y,z,p+1) and f(x,y+2,z,p+1) and f(x,y,z+2,p+1)


# print(([i for i in range(1, 20) if f(2, 3, i, 0)]))


# def f(x, y, z, p):
#     if (x >= 20 or y >= 20 or z >= 20 or x+y+z >= 25) or p > 3:
#         return p == 3
#     if p % 2 == 0: 
#         return f(x*2,y,z,p+1) or f(x,y*2,z,p+1) or f(x,y,z*2,p+1) or f(x+2,y,z,p+1) or f(x,y+2,z,p+1) or f(x,y,z+2,p+1)
#     else:
#         return f(x*2,y,z,p+1) and f(x,y*2,z,p+1) and f(x,y,z*2,p+1) and f(x+2,y,z,p+1) and f(x,y+2,z,p+1) and f(x,y,z+2,p+1)


# print(([i for i in range(1, 20) if f(2, 3, i, 0)]))


def f(x, y, z, p):
    if (x >= 20 or y >= 20 or z >= 20 or x+y+z >= 25) or p > 4:
        return p == 2 or p == 4
    if p % 2: 
        return f(x*2,y,z,p+1) or f(x,y*2,z,p+1) or f(x,y,z*2,p+1) or f(x+2,y,z,p+1) or f(x,y+2,z,p+1) or f(x,y,z+2,p+1)
    else:
        return f(x*2,y,z,p+1) and f(x,y*2,z,p+1) and f(x,y,z*2,p+1) and f(x+2,y,z,p+1) and f(x,y+2,z,p+1) and f(x,y,z+2,p+1)


print(([i for i in range(1, 20) if f(2, 3, i, 0)]))
