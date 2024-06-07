for x in '0123456789abcdefghijklmnopqrstuvwxyz':
    s = int(f'i{x}', 36) + int(f'L{x}VE', 36) + int('ANIME', 36)
    if int(s) % 25 == 0:
        print(int(s) / 25)