def f(a, n): # 20
    if a >= 301 and n == 3:
        return True
    if a >= 301 and n == 1:
        return False
    if a < 301 and n == 3:
        return False


def f(a, n):
    if a >= 31 and n == 3:
        return True
    if a >= 31 and n != 3:
        return False
    if a < 31 and n == 3:
        return False

    if n % 2 == 1:  # был ход Пети
        return f(a + 1, n + 1) and f(a * 2, n + 1)
    return f(a + 1, n + 1) or f(a * 2, n + 1)


for s in range(1, 30 + 1):
    if f(s, 0):
        print(s)