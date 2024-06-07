s = open('aintens/variant4/24_15339.txt').readline()
s = s.replace('B','A')
s = s.replace('C','A')
s = s.replace('7','6')
s = s.replace('8','6')
s = s.replace('9','6')
s1 = ''
data = []
for x in s :
    s1 += x
    if 'AA' in s1 or '66' in s1: 
        data.append(len(s1) - 1)
        s1 = s1[-1]
print(max(data))

    