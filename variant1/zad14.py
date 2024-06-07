for x in '01234567890abcde':
    s = int(f'1{x}51', 15) - int(f'3{x}2', 15)
    if s % 4 == 0:
        print(s // 4)