# все общие делители (включая 1 и само число)
# n = 36
# divs = []
# for div in range(1, n + 1):
#     if n % div == 0:
#         divs.append(div)
# print(divs)

# все общие делители
def f(n):
    divs = []
    for div in range(1, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.append(div)
            if div != n // div:
                divs.append(n // div)
    return sorted(divs) # максимум



# # извлекался ли корень из числа
# if len(divs) % 2 == 1:
#     print('извлекался')

