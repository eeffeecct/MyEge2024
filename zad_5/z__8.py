for n in range(2, 1000):
    s = bin(n)[2:]
    s = s[:-1] + s[1] * 2
    if int(s, 2) > 92:
        print(int(s, 2))
        break

# otvet: 99
