s = open('probnik6/24.txt').readline().split('2')
data = []
for x in s: 
    k = 0
    for i in x: 
        if i in 'KNLF': 
            k += 1
        if len(x) == k:
            data.append(k)

s = open('probnik6/24.txt').readline().split('4')
for x in s: 
    k = 0
    for i in x: 
        if i in 'KNLF': 
            k += 1
        if len(x) == k:
            data.append(k)

s = open('probnik6/24.txt').readline().split('6')
for x in s: 
    k = 0
    for i in x: 
        if i in 'KNLF': 
            k += 1
        if len(x) == k:
            data.append(k)

s = open('probnik6/24.txt').readline().split('8')
for x in s: 
    k = 0
    for i in x: 
        if i in 'KNLF': 
            k += 1
        if len(x) == k:
            data.append(k)

s = open('probnik6/24.txt').readline().split('0')
for x in s: 
    k = 0
    for i in x: 
        if i in 'KNLF': 
            k += 1
        if len(x) == k:
            data.append(k)
print(max(data))