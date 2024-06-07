def f(n):
    n17 = ''
    while n: 
        n17 = str(n % 17) + ' ' + n17
        n //= 17
    return n17

n = 12 * 19**1667 + 2 * 21**1729 + 7 * 13**1820 - 1915
k = 0
for x in f(n): 
    if x in '2': 
        k += 2
    elif x in '3':
        k += 3
    elif x in '5':
        k += 5
    elif x in '7':
        k += 7
    elif x in '11':
        k += 11
    elif x in '13':
        k += 13
        
print(k)
