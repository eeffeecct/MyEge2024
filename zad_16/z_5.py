def f(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return f(n / 2)
    elif n > 0 and n % 2 != 0:
        return f(n - 1) + 3


data = 0
for i in range(1, 1001):
    if f(i) == 18:
        data += 1
print(data)
# otvet: 209
