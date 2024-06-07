s = '4' * 60 + '6' * 80 + '8' * 60
while '46' in s or '84' in s or '86' in s:
    if '46' in s:
        s = s.replace('46', '64', 1)
    if '84' in s:
        s = s.replace('84', '48', 1)
    if '86' in s:
        s = s.replace('86', '68', 1)
data = list(s)
print(data[24], data[74], data[149])