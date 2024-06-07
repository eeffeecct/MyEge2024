def is_prime(n):
    for div in range(2, n // 2 + 1):
        if n % div == 0:
            return False
    return True

for n in range(10, 100):
    if is_prime(n):
        print(n)