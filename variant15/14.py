for x in 'abcdefghijklmnopqrstuvw':
    n = int(f'9{x}38{x}93', 33) + int(f'832{x}7{x}', 33) 
    if n % 32 == 0: 
        print(n / 32)