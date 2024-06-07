for a in range(0, 1000):
    if not any((3 * x + y > a) and (y < x) and (x < 30) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
        break