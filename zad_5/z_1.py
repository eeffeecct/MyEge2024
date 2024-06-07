for n in range(1, 1000):
    s = bin(n)[2:]
    a = s.count('1')
    s += str(int(a % 2))
    s += str(int(a % 2))
    if int(s, 2) > 97:
        print(n)
        break
# otvet: 25
