from fnmatch import fnmatch
import math

def f(n):
    divs = []
    for div in range(1, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.append(div)
            if div != n // div:
                divs.append(n // div)
    return sorted(divs)

def s(n):
    num = math.isqrt(n)
    if num * num == n:
        return True
    else: 
        return False 


for n in range(650000, 10**9 ):
    summa = f(n)[0] + f(n)[-1]
    if fnmatch(str(n), '13*4') and s(summa) == True:
        print(n, summa)
