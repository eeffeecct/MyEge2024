for a in range(1,1000):
    if all(((x % 10 == 0) <= ((x > 70) or (a < x + 10))) for x in range(1, 1000)):
        print(a)