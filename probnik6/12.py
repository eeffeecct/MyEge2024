def f(n):
    res = [int(i)**2 for i in n]
    return sum(res)



for n in range(5, 987):
    data = []
    s = '5' + n*'7'
    while '57' in s or '777' in s or '79' in s:
        if '57' in s: 
            s = s.replace('57','7',1)
        if '777' in s: 
            s = s.replace('777','97',1)
        if '79' in s: 
            s = s.replace('79','5',1)
    data.append(f(s))
print(max(data))