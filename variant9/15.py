for a in range(-100, 1000):
    if all(((x*y<=a+13) <= ((28*y>520) or (x*25>800))) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
