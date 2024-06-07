f = open('zad_27/9755/27_A_9755.txt')
k = 155
n = 775

data = [int(x) for x in f]
kmin = 1000000
for i in range(n): 
    for j in range(i+1,n):
        for p in range(j+1,n):
            if j-i>=k and p-j>=k:
                kmin = min(kmin, data[i] + data[j] + data[p])
print(kmin)