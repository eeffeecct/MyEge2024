for x in '01234567890abcdefghijklmnopqrstuvwx':
    n = (int(f'tl{x}32', 35) + int(f'12{x}WA',35))
    if n % 34 == 0:
        print(n / 34)
        