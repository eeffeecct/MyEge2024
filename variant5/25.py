def f(n):
    divs = []
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.append(div)
            if div != n // div:
                divs.append(n // div)
    return divs


for i in range(123456, 987655):
    if len(f(i)) == 3:
        print(sorted(f(i))[-1], i)


