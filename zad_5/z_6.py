for n in range(2, 1000):
    s = bin(n)[2:]
    s += s[1] + s[0]
    if int(s, 2) > 90:
        print(n)
        break

# otvet: 23