s = open('variant6/24.txt').readline()
data = [0]
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        data[-1] += 1
    else:
        data.append(0)
print(max(data))
