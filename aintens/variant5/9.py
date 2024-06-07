k = 0
for line in open('aintens/variant5/9.csv'):
    data = list(map(int, line.split(',')))
    rep = [x for x in data if data.count(x)==2]
    n_rep = [x for x in data if data.count(x)==1]
    try:
        sr_zn = (max(rep) + min(rep))/2
        if len(rep) == 6 and sr_zn < sum(n_rep):
            k += 1
    except:
        continue
print(k)