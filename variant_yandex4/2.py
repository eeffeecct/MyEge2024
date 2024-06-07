print('k l m n')
for k in range(2):
    for l in range(2):
        for m in range(2):
            for n in range(2):
                if not((not n) or k and (not m) or (l == m)):
                    print(k,l,m,n)
                    