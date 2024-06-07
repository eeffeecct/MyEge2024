for x in range(1, 201):
    f = [0] * 3003
    for n in range(3002, 1, -1):
        if n >= 3000:
            f[n] = n
        else:
            f[n] = n - 2 * x + f[n + 2]
    if f[28] - f[34] == 324:
        print(x)
        break