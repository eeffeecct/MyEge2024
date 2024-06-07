text = open('1.txt').readline()
k = 1
data = []
for i in range(len(text) - 1):
    if text[i] != text[i-1]:
        k += 1
    else:
        data.append(k)
        k = 1
print(max(data))
# 35
