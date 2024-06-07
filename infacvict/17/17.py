# s = [int(x) for x in open('17-4.txt')]  # default every 17 zadanie
# numbers = []
# for c in s:
#     if c % 13 == 4 and c % 8 == 1:
#         numbers.append(c)
# print(max(numbers), sum(numbers))   # 8649 97979

# s = [int(x) for x in open('17-4.txt')]
# numbers = []
# for i in s:
#     if i > 100 and str(i)[-2] in '01234' and str(i)[-3] in '34567':
#         numbers.append(i)
# print(len(numbers), min(numbers))

# def to3(n):
#     n3 = ''
#     while n:
#         n3 = str(n % 3) + n3
#         n //= 3
#     return n3
#
#
# s = [int(x) for x in open('17-4.txt')]
# numbers = []
# for i in s:
#     if sum(map(int, str(i))) % 5 == 0 and to3(i)[-2:] != '00':
#         numbers.append(i)
# print(len(numbers), max(numbers))

# s = [int(x) for x in open('17-205.txt')]
#
# data = []
# for i in range(len(s) - 1):
#     if (s[i] % 7 == 0 or s[i+1] % 7 == 0) and str(s[i] + s[i+1])[-2:] == '19':
#         data.append(s[i] + s[i+1])
# print(len(data), max(data))

s = [int(x) for x in open('17-205.txt')]

data = []
for i in range(len(s) - 1):
    if (s[i] % 10 == 7 or s[i+1] % 10 == 7) and (s[i] + s[i+1]) % 12 == 0:
        data.append(s[i] + s[i+1])
print(len(data), max(data))
