for n in range(1, 1000):
    s = bin(n)[2:]
    if int(s) % 2 == 0:
        s = '10' + s 
    else: 
        s = '1' + s + '01'

    if int(s, 2) > 516:
        print(n)
        break

