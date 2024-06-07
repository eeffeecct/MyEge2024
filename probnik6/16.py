import math

f = [0] * 2025
for n in range(1, 2024 , 1):
    if n > 2024:
        f[n] = math.factorial(n**2)
    else:
        f[n] = f[n+1] + n**2 - 1
print(f[1001]-f[1004])
