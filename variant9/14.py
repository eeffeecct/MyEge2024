def base7(n):
    n7 = ''
    while n:
        n7 = str(n % 7) + n7
        n //= 7
    return n7


# data = []
# for x in range(1, 1000):
#     s = f(7**500 + 7**200 - 7**50 - x)
#     if int(s) >= 0:
#         data.append(sum(map(int, s)))
# print(max(data))

expression_result = 7**500 + 7**200 - 7**50
x = 0  # Максимальное значение x
number_in_base_7 = base7(expression_result - x)
sum_of_digits = sum(int(digit) for digit in str(number_in_base_7))
print("Максимальная сумма разрядов:", sum_of_digits)
