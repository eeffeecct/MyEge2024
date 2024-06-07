mn = []
k = 0

for l in open('9.csv'):
    l = [int(x) for x in l.split(',')]
    k += 1
    nr = [x for x in l if l.count(x) == 1]
    r = [x for x in l if l.count(x) > 1]

    if len(r) > 0:
        if sum(r) % len(nr) != 0:
            if sum(nr) > sum(r):
                if sum(l) == 129:
                    print(k)
                    break

