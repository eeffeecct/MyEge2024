print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (not(w == y)) and (z <= w) and (not x):
                    print(x, y, w, z)
