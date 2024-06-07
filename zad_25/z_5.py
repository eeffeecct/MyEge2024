from fnmatch import fnmatch


def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n // i == i:
                count += 1
            else:
                count += 2
    return count


for num in range(1, 10**9):
    if count_divisors(num) == 9:
        if fnmatch(str(num), '15*3*09'):
            print(num)
