for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0: 
        s = '1' + s + '1'
    else:
        s += '10'
    if int(s, 2) > 179:
        print(n)
        break
    