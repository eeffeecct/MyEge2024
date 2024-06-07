def f(n): 
    n2 = ''
    while n: 
        n2 = str(n % 27) + ' ' + n2
        n //= 27
    return n2

n = 2*729**2014+2*243**2016-2*81**2018+2*27**2020-2*9**2022-2024
k = 0

for n in f(n).split(): 
    if int(n) > 9: 
        k += 1
print(k)