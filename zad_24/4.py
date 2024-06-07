text = open('4.txt').readline()
k = 0
data = []
for i in text:
    if i != 'C' and i != 'F':
        k += 1
    else:
        data.append(k)
        k = 0
print(max(data))
# 19
