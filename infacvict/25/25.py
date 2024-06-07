# def f(n):
#     divs = []
#     for div in range(1, int(n ** 0.5) + 1):
#         if n % div == 0:
#             divs.append(div)
#             if len(divs) > 4: break
#             if div != n // div:
#                 divs.append(n // div)
#     return sorted(divs)


# for i in range(251811, 251827):
#     if len(f(i)) == 4:
#         print(f(i)[-2], f(i)[-1])


# def f(n):
#     divs = []
#     for div in range(1, int(n ** 0.5) + 1):
#         if n % div == 0:
#             divs.append(div)
#             if div != n // div:
#                 divs.append(n // div)
#     return sorted(divs)


# max_divs = []
# for i in range(394441, 394506):
#     d = f(i)
#     if len(d) >= len(max_divs):
#         max_divs = d
#     print(len(max_divs), max_divs[-1])

def is_prime(n):
    for div in range(2, n // 2 + 1):
        if n % div == 0:
            return False
    return True

k = 0
for i in range(2532421, 2532492):

    if is_prime(i):
        k += 1
        print(k, i)



