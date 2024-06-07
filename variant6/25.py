from fnmatch import *

def f(n):
    divs = []
    for div in  range(1, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.append(div)
            if div != n // div:
                divs.append(n // div)
    return divs


for i in range(2025, 10**9, 2025):
    if fnmatch(str(i), '*8?8?5') and len(f(i)) == 64:
        print(i, i//2025)