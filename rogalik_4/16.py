def f(n):
    print('*')
    if n > 1:
        f(n - 2)
        f(n // 2)
        print('*')
    print('*')


print(f(127))
