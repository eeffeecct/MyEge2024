s = [int(x) for x in open('variant15/17_16346.txt')]
minim = 52
data = []
for i in range(len(s) - 1):
    u = (abs(s[i]) % 100 == minim) + (abs(s[i+1]) % 100 == minim)
    if u >= 1:
        data.append(s[i]**2 + s[i+1]**2)
print(len(data), min(data))