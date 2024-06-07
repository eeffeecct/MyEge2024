for x in '0123456789abcde':
    n = int(f'99658{x}29', 15) + int(f'102{x}023', 15)
    if n % 14 == 0: 
        print(n // 14)