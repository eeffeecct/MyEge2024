f = open('zad_27/2257/27B_2257.txt')

n = int(f.readline()) # кол-во чисел 
li = [int(x) for x in f] 
pref = {0: 0}
s = k = 0
res = []

for x in li:
    s += x
    if x % 2 == 0:
        k += 1
    if k % 10 not in pref:
        pref[k % 10] = s
    else:
        res.append(s - pref[k % 10]) # текущ сумм - префикс
print(max(res))
