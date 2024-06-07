text = open('2.txt').readline()
k = 0
data = []
for i in text:
    if i in 'ACD':
        k += 1
    else:
        data.append(k)
        k = 0
print(max(data))
# 11
