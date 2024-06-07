s = '>' + 26*'1' + 10*'2' + 14*'3'

while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s :
        s = s.replace('>1', '22>', 1)
    elif '>2' in s:
        s = s.replace('>2', '2>', 1)
    elif '>3' in s:
        s = s.replace('>3', '1>', 1)
print(s)
s = '2222222222222222222222222222222222222222222222222222222222222211111111111111'
print(sum(map(int, s)))
