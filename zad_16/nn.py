#from sys import setrecursionlimit
#setrecursionlimit(5000)
#
#def f(n):
#    if n <= 3:
#        return 1
#    if n > 3:
#        return (n + 3) * f(n - 2)
#
#
#print(f(2028) // f(2024))
#



f = [0] * 2029
for n in range(1, 2029, 1):
    if n <= 3:
        f[n] = 1
    if n > 3:
        f[n] = (n + 3) * (n - 2)
print(f[2028] // 2024)