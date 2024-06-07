
li = [10, 10, 10, 10, 2, 30, 20, 7, 10,10,10,10,10]
pref = {0: (0, 0)}
s = k = 0
res = []
for x in li:
    s += x
    k += 1
    if s % 10 not in pref:
        pref[s % 10] = (s, k)
        print(pref)
    else:
        res.append((s - pref[s % 10][0], k - pref[s % 10][1]))
res.sort(reverse=True)
print(res[:5])
