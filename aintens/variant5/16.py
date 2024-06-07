from sys import setrecursionlimit
def f(n):
    if n <= 3:
        return 1
    else: 
        return (n+3) * f(n-2)
setrecursionlimit(3000)
print(f(2028)//f(2024))