for x in '0123456789abcde':
    n = int(f'z{x}c12',36) + int(f'137{x}ea',15)
    if n % 7 == 0:
        print(x, n // 7)