for m in range(1, 1000):
    divs = []
    s = '>' + 15*'1' + 35*'2' + m*'3'
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        elif '>2' in s:
            s = s.replace('>2', '3>', 1)
        elif '>3' in s:
            s = s.replace('>3', '11>')

    n = sum(map(int, s[:-1]))
    for div in range(1, n + 1):
        if n % div == 0:
            divs.append(div)
    print(m, divs, len(divs))
    if len(divs) == 5:
        print(m)
        break