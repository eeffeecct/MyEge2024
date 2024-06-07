f = open('aintens/variant3/24_16333.txt').readline()
f = f.replace('R', 'Q')
f = f.replace('W', 'Q')
f = f.replace('2', '1')
f = f.replace('4', '1')
data = []
s = ''
for x in f:
    s += x
    if 'QQ' in s or '11' in s: 
        s = s[-1]
    data.append(len(s))
print(max(data))
