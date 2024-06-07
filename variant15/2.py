print('v w x y z')
for v in range(2):
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    if not((w <= (v == x)) or (y and (not x))) and (not z): 
                        print(v,w,x,y,z)
                        