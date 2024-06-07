# for x in '0123456789abcdefghijklmnopq':
#     n = int(f'123{x}24', 27) + int(f'135{x}78', 27)
#     if n % 26 == 0:
#         print(n // 26)


for a in range(1, 1000):
    if all((x % a != 0) <= ((x % 28 == 0) <= (x % 49 != 0)) for x in range(1,1000)):
        print(a)