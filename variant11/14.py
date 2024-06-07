for n in range(6, 37):
    s = 7**500 - int('53', n)
    if s % 6 == 0: 
        print(n)
        break
