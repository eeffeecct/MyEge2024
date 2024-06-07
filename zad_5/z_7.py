for n in range(128, 256):
    s = bin(n)[2:]
    s = s.replace('1', '$')
    s = s.replace('0', '1')
    s = s.replace('$', '0')
    if n - int(s, 2) == 185:
        print(n)

# otvet: 220
