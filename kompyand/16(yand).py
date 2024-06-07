from sys import setrecursionlimit
def f(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 2 == 0 :
        return n//2*f(n-1)
    else:
        return (n-1)//2*f(n-1)
setrecursionlimit(3000)
print((f(2024)-f(2022))//f(2021))
