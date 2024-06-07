for x in '0123456789abcdefghijklmno':
    n = int(f'12373{x}57',25) + int(f'142{x}23',25) + int(f'1{x}34561', 25)
    if n % 24 == 0:
        print(n / 24)