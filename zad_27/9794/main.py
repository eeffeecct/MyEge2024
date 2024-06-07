# k = 100
# n= 5
# data = [20,50,50,100,200]

f = open('zad_27/9794/27_A_9794.txt')
k = int(f.readline())
n = int(f.readline())
data = [int(x) for x in f]

a = 0

for i in range(n):
    for j in range(i+1,n):
        if data[i] + data[j]>=k:
            a += 1

print(a)