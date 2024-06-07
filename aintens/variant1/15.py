for a in range(1,1000):
    if all( ((x % 15 == 0) and (x % 10 != 0)) <= (a < x + 50) for x in range(1, 1000)):
        print(a)