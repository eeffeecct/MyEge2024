for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 3 == 0: 
        s += s[-2:]
    else: 
        s += bin((n%3)*3)[2:]
    if int(s,2) >= 120:
        print(n)
        break