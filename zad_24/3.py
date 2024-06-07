text = open('3.txt').readline()
k = 0
data = []
for i in text:
    if i != 'D':
        k += 1
    else:
        data.append(k)
        k = 0
print(max(data))
# 44
