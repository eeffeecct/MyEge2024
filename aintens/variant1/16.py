import math 
def s(n):
    num = math.isqrt(n)
    if num * num == n:
        return True
    else: 
        return False 

def f(n):
    if n <= 5:
        return n
    elif n > 5 and n % 2 == 0:
        return 2*f(n-1)-f(n//2)
    elif n > 5 and n % 2 != 0:
        return f(n-2)+f(n % 5) + f(n // 5)


for n in range(1, 10000):
    if len(str(f(n))) == 4 and s(f(n)):
        print(n)
        