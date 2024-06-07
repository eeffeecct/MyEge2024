n = 128 * '1'
k = 0
while '333' in n or '11' in n:
    if '333' in n: 
        n = n.replace('333', '1', 1)
        
    else:
        n = n.replace('11', '3', 1)
        k += 2
print(k)

