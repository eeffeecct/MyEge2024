def f(x,y,p): # 21
    if x * y >= 123 or p > 4: 
        return p == 2 or p == 4
    if p % 2:
        return f(x + 2, y, p + 1) or f(x * 2, y, p + 1) or \
          f(x, y + 2, p + 1) or f(x,y*2,p+1)
    else: 
        return f(x + 2, y, p + 1) and f(x * 2, y, p + 1) and \
          f(x, y + 2, p + 1) and f(x,y*2,p+1)
print(max([i for i in range(1, 41) if f(3, i, 0)]))