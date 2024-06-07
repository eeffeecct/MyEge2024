data = []
for x in '0123456789abcdefg':
    for y in '0123456789abcdefghijkl':
        f1 = int(f'5{x}{x}78', 17)
        f2 = int(f'4{x}{x}9', 18)
        f3 = int(f'88{x}{x}5', 19)
        f4 = int(f'6{x}{y}23', 22)
        if (f1 + f2 + f3 - f4) % 405 == 0 and f1 + f2 + f3 - f4 > 0:
            data.append(int(y, 22) * x)

print(max(data))