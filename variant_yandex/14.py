def sorokdev(x):
    n49 = []
    while x > 0:
        n49.append(str(x % 49) + str(n49))
        x //= 49
    return n49


x = 18 * 7 ** 108 - 5 * 49 ** 76 + 343 ** 35 - 50
a = sorokdev(abs(x))

print(sum(map(int, a)))
