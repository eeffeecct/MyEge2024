s = [int(x) for x in open('D:/Python/ege/variant4/17_6605.txt')]
data = []
maxi = [j for j in s if str(abs(j))[-1] == '5']
maxi = max(maxi)

for i in range(len(s) - 1):
    condition = (str(s[i])[-1] == '5') + (str(s[i+1])[-1] == '5')
    if condition == 1 and (s[i] ** 2 - s[i+1] ** 2) <= maxi**2:
        data.append(abs(s[i] ** 2 - s[i+1] ** 2))
print(len(data), max(data))
