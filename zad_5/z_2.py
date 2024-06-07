for n in range(1, 1000):
    s = bin(n)[2:]
    s += str(int(s.count('1') % 2))
    s += str(int(s.count('1') % 2))
    if int(s, 2) > 123:
        print(int(s, 2))
        break
        
# otevt: 126
