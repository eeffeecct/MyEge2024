def is_prime(n):
    for div in range(2, n // 2 + 1):
        if n % div == 0:
            return False
    return True


alph = '0123456789abcdefgh'
k = 0
for x in alph:
    if is_prime(int(f'56{x}3', 18) + int(f'4{x}9', 18) - int(f'57{x}1', 18)):
        k += 1
print(k)