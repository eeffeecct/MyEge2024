# for x in '0123456789abcdefghi':
#     n = int(f'98{x}79641',19) + int(f'36{x}14',19) + int(f'73{x}4',19)
#     if n % 18 == 0:
#         print(n // 18)

for x in range(0, 68):
    n1 = 1*68**4 + 2*68**3 + 3*68**2 + x*68**1 + 5*68**0
    n2 = 1*68**4 + x*68**3 + 2*68**2 + 3*68**1 + 3*68**0
    if (n1 + n2) % 12 == 0:
        print((n1 + n2)//12)