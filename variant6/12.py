k = 0
for n in range(10, 101):
    s = '4' + n*'5'
    while '45' in s or '222' in s:
        if '45' in s:
            s = s.replace('45', '2', 1)
        elif '222' in s:
            s = s.replace('222', '4', 1)
    if sum(map(int, str(s))) % 2 == 0:
        k += 1
print(k)
