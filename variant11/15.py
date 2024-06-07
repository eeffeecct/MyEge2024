for a in range(0, 1000):
    if all((((x & 103 == 0) and (x & 94 != 0)) <= (x & a != 0)) for x in range(1, 1000)):
        print(a)
        break