from fnmatch import fnmatch 
from functools import lru_cache

@lru_cache
def f(n):
    divs = []
    for div in range(1, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.append(div)
            if div != n // div:
                divs.append(n // div)
    
    return divs


for i in range(13052774, 13892736):
    if fnmatch(str(i), '13*7?5') and len(f(i)) == 62 and sum(f(i)) % 2024 == 0:
        print(i, sorted(f(i))[-2])
        
