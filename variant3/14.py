def f(n):
    n7 = ''
    while n > 0:
        n7 = str(n % 7) + n7
        n = n // 7
    return n7


k = 0
s = list(f(343**515 - 6 * 49**520 + 5*49**510 - 3 * 7**530 -550))
for i in range(len(s)):
    if s[i] == '6':
        k += 1
print(k)
