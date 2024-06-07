s = '7'*25 + '4'*19 + '5'*23
data = []
while '75' in s or '74' in s: 
    if '75' in s: 
        s = s.replace('75', '55', 1)
    else: 
        s = s.replace('74', '475', 1)
    data.append(s.count('5'))
print(max(data))
    