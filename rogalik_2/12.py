s = '111' * 7 + 40 * '000'
while '11' in s or '00' in s:
    if '11' in s:
        s = s.replace('11', '10', 1)
    if '00' in s:
        s = s.replace('00', '0', 1)
print(s.count('1'))