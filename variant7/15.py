for a in range(1, 100):
    if all(((x % 12 == 0) and (x & 4==0)) <= (x + 1 > a) for x in range(1, 100)):
        print(a)
