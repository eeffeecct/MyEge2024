f = open('26sisadmin.txt')
s,n = map(int, f.readline().split())

files = [int(x) for x in f]
files.sort()
res = []
for x in files:
    if s - (sum(res) + x) >= 0:
        res.append(x)
    elif s - sum(res[:-1]) - x >= 0:
        res[-1] = x
print(len(res), res[-1])
