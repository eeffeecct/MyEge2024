f = [0] * 2024
for n in range(1, 2023 + 1, 1):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = n * f[n-1]
print(f[2023] // f[2020])
