for x in '0123456789abcdefghijkl':
    s = int(f'98{x}79641', 22) + int(f'36{x}14', 22) + int(f'73{x}4', 22)
    if int(s) % 21 == 0:
        print(int(s) / 21)
