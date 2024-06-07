def f(n):
    divs = []
    for div in range(1, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.append(div)
            if div != n // div:
                divs.append(n // div)
    return sorted(divs) 

n = 600001
while n < 600500: 
    s = f(n)
    for a in s:
        if a % 10 == 9 and a != 9 and a != n:
            print(n, s)
    n += 1


