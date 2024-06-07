def g(n): 
    if n < 10: 
        return n
    else: 
        return g(n-2) + 1
    
def f(n): 
    return g(n-1)

k = 0
for n in range(1, 101):
    x = f(n)
    if int(x**0.5)**2 == x and x > 0:
        k += 1
print(k)
