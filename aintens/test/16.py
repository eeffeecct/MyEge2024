from sys import setrecursionlimit
# f = [0] * 2027
# for n in range(2025, 1, -1):
#     if n >= 2025:
#         f[n] = n
#     else:
#         f[n] = f[n + 1] - f[n + 2] + 7
# print(f[15] - f[24]) 

# def f(n): 
#     if n < 2 : 
#         return 1
#     elif n > 2: 
#         return 2 * f(n-1) - f(n-2) + n
    
# setrecursionlimit(100000)
# print(f(5994) - f(5990) - 4*(f(5991) - f(5990)))

def f(n):
    if n == 1: 
        return 1
    elif n == 2:
        return 2
    elif n > 2 and n % 2 == 0: 
        return (8*n+f(n-3))//9
    elif n > 2 and n % 2 != 0: 
        return (4*n+f(n-1)+f(n-2))/7
    
print(f(52) )   
