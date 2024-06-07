for a in range(0, 100):
    if all(((x & 84 == 0) <= (x & 13 != 0)) <= (x & a != 0) for x in range(0,100)):
        print(a)
        break