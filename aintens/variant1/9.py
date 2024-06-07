f = open('aintens/variant1/9.csv')
k = 0
for s in f:
    k += 1
    data = list((int(i) for i in s.split(', ')))
    data1 = sorted(data)
    if data[0] < data[1] < data[2] < data[3] < data[4] < data[5] and \
        (data1[0] + data[5])*2 > data[1] + data[2] + data[3] + data[4]:
        print(k)
