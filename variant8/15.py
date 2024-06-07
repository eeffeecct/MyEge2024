from math import gcd
k = 0
for a in range(1, 1001):
    if all(gcd(a, 420) == 2 or ((not gcd(a, x) == 12) <= (not gcd(110, x) == 11)) for x in range(1,1000)):
        k += 1
print(k)
