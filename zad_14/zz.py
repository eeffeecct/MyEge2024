def f(n):
    n15 = ''
    while n:
        n15 = str(n % 15) + ' ' + n15
        n //= 15
    print(n15)
    return n15

n = 11*15**65+18*15**38-14*15**17+19*15**11+18338
data = []
for i in f(n).split():
    print(f(n).split())
    if i not in data:
        data.append(i)

print(len(data))


