data = set()
for n in range(10, 1000):
    s = bin(n)[3:]
    res = int(s, 2) - n
    data.add(res)
print(len(data))

# otvet: 7
