k = 0
for l in open('variant7/9_9878.csv'):
    k += 1
    l = [int(x) for x in l.split(',')]
    n3 = [x for x in l if l.count(x) == 3] # повтор 3 раза
    n1 = [x for x in l if l.count(x) == 1]
    if len(n3) + 1 == len(n1):
        print(n3, n1, k)

