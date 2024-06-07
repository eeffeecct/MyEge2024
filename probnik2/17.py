s = [int(i) for i in open('17.txt')]
maxi = max([i for i in s if abs(i) % 10 == 9 and 100 <= abs(i) <= 999])
data = []
for i in range(len(s) - 1):
    usl1 = (100<=abs(s[i])<=999 and s[i] % 10 == 9) + (100<=abs(s[i+1])<=999 and s[i+1] % 10 == 9)
    if (usl1 == 1 or usl1 == 0) and (s[i] + s[i+1] >= maxi):
        data.append(s[i] + s[i + 1])
print(len(data), max(data))
