# from itertools import * 
# k = 0 

# for i in product(range(9), repeat=6): 
#     chet = [j for j in i if j % 2 == 0] 
#     if i[0] != 0 and len(chet) <= 2 and i[-1] % 2 == 0: 
#         k += 1 
# print(k) 

def f(n):
    n9 = ''
    while n:
        n9 = str(n % 9) + n9
        n //= 9
    return n9

k = 0
for i in range(9**5, 9**6):
    s = f(i)
    chet = [j for j in s if int(j) % 2 == 0] 
    if len(chet) <= 2 and i % 2 == 0:
        k += 1
print(k)
