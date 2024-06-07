def f(n):
    n25 = ''
    while n:
        n25 = str(n % 25) + ' ' + n25
        n //= 25
    return n25


n = 13037115627
k = 0
for i in f(n).split():
    if i == '0':
        k +=1
print(k)


# 9




