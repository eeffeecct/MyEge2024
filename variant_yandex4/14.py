for x in '0123456789abcdefghijklmnopqrs':
    n = int(f'42{x}158', 29) + int(f'16{x}234', 29)
    if n % 28 == 0:
        print(n / 28)

