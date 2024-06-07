for a in range(0, 1000):
    if all(((x&52!=0) and (x&36==0)) <= (x&a!=0) for x in range(0, 1000)):
        print(a)
        break
