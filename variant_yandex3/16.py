f = [0] * 2030
for i in range(2029, 1, -1):
    if i >= 2024:
        f[i] = 1
    else:
        f[i] = f[i + 2] + f[i + 4]
print(len(set(f)))
