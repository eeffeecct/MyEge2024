def f(n):
    n27 = ''
    while n:
        n27 = str(n % 27) + ' ' + n27
        n //= 27
    return n27

s = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 - 4*3**2024 - 2029
s = f(s).split()
k = 0

for i in s:
    if int(i) > 9:
        k += 1
print(k)
