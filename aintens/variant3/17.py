s = [int(x) for x in open('aintens/variant3/17_16328.txt')]
minim = min([x for x in s if x % 19 == 0])
data = []
for i in range(len(s) - 1):
    usl = (s[i] % minim == 0) + (s[i+1] % minim == 0)
    if usl >= 1: 
        data.append(s[i] + s[i+1])
print(len(data), max(data))