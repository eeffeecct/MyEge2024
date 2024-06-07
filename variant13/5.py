for n in range(1, 1000): 
    s = bin(n)[2:]
    if n % 8 == 0: 
        s += s[-2:]
    else: 
        s += bin((n % 8) * 2)[2:]
    if int(s,2) > 3000:
        print(n)
        break