from fnmatch import fnmatch

def f(n):
    divs = []
    for div in range(1, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.append(div)
            if div != n // div:
                divs.append(n // div)
    return divs



for i in range(500000, 500115):
    if fnmatch(str(sum(f(i))), '*7?'):
        print(i,sum(f(i)))

