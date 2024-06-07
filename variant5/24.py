s = [i for i in open('24.txt')]


k = 0
data = []
while 'XZZY' in str(s):
    if 'XZZY' in str(s):
        s = str(s).replace('XZZY', '*', 1)

for i in s:
    if i != '*':
        k += 1
    elif i == '*':
        data.append(k)
        k = 0

print(max(data))