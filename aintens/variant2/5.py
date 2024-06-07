def f(n):
    n7 = ''
    while n: 
        n7 = str(n % 7) + n7
        n //= 7
    return n7

data = []
data1 = []
for n in range(16, 1000):
    s = f(n)    
    if sum(map(int, s)) % 5 == 0:
        s += '6'
    else: 
        s += str(sum(map(int, s)) % 5)
    if int(s) < 567:
        data.append(int(s))
        data1.append(int(s, 7))
print(max(data))
print(data)
print(data1)
