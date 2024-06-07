from sys import setrecursionlimit
def f(n):
    if n <= 3: 
        return n
    elif n > 3 and n % 2 != 0:
        return 2*n + f(n-2)
    elif n > 3 and n % 2 == 0:
        return n**2+f(n-1)
setrecursionlimit(6000)
print(f(10000) - f(9995))
