for a in range(0, 1000):
    if all((y >= 2*x +19) or (5*x >= a*y-20)or(5*y+8*x>=24) for x in range(0, 1000) for y in range(0,1000)) :
        print(a)