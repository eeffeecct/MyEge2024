with open('variant12/26_11894.txt') as f:
    n, k = [int(x) for x in f.readline().split()] # 10000, 100
    data = [[int(x) for x in s.split()] for s in f] # сколько нужно, прибавка
   
data.sort()
count = 0
for x in data:
    sk, add = x[0], x[1] # сколько нужно, прибавка
    if sk <= k:
        count += 1
        k += add
print(count, k)