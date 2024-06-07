for x in '0123456789abcdefghijklmnopqrstu':
    if (int(f'12373{x}57', 31) + int(f'142{x}23', 31) + int(f'1{x}34561', 31)) % 30 == 0:
        print((int(f'12373{x}57', 31) + int(f'142{x}23', 31) + int(f'1{x}34561', 31)) / 30)