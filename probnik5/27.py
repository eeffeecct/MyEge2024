n = 652
data = []
s = [int(x) for x in open('probnik5/27a.txt').readlines()]
for i in range(len(s)):
    summa = 0
    kolvo = 0
    for j in range(i,n):
        summa += s[j]
        kolvo += 1
        if summa == 2729288 and summa % 157 == 0:
            print(kolvo)

