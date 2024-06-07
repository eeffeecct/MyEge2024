text = open('7.txt').readline()
k = 0
data = set()
for i in range(len(text) - 1):
    if (text[i] != 'P' or text[i+1] != 'R') and (text[i] != 'R' or text[i+1] != 'P'):
        k += 1
    else:
        data.add(k)
        k = 0
print(max(data))
# 2939
