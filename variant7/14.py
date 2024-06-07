for x in '123456789':
    s = int(f'72{x}', 32) + int(f'1c{x}7', 32) + int(x)**5
    print(s / int(x), x)


