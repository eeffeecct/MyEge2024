f = open('aintens/variant2/9.csv')
k = 0
for s in f:
    data = list((int(i) for i in s.split(',')))
    summa = sum(data)
    if max(data) > min(data)*2 and \
        (summa % data[0] == 0 or summa % data[1] == 0 or summa % data[2] == 0 or summa % data[3] == 0 or summa % data[4] == 0):
        k += 1
print(k)
