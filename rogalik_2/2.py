print('c x z')
for c in range(2):
    for x in range(2):
        for z in range(2):
            if (((not x) and z) or c) and (not (x and z)):
                print(c, x, z)
