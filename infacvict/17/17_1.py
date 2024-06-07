# def to3(n):
#     n3 = ''
#     while n:
#         n3 = str(n % 3) + n3
#         n //= 3
#     return n3
#
#
# def to5(n):
#     n5 = ''
#     while n:
#         n5 = str(n % 5) + n5
#         n //= 5
#     return n5
#
#
# s = [int(x) for x in open('17-4.txt')]
# data = []
# for i in s:
#     if to3(i)[-1] == to5(i)[-1] and (i % 31 == 0 or i % 47 == 0 or i % 53 == 0):
#         data.append(i)
# print(len(data), min(data))

# s = [int(x) for x in open('17-4.txt')]
#
#
# def to5(n):
#     n5 = ''
#     while n:
#         n5 = str(n % 5) + n5
#         n //= 5
#     return n5
#
#
# data = []
# for i in s:
#     if (bin(i)[2:])[-4:] == '1001' and to5(i)[-2:] == '11':
#         data.append(i)
# print(max(data), sum(data))

# s = [int(x) for x in open('17-205.txt')]
#
# data = []
# for i in range(len(s) - 1):
#     if (s[i] % 10 == 7 or s[i+1] % 10 == 7) and (s[i] + s[i+1]) % 12 == 0:
#         data.append(s[i] + s[i+1])
# print(len(data), max(data))

# s = [int(x) for x in open('17-4.txt')]
#
# data = []
# sr = sum(s) / len(s)
# for i in range(len(s) - 1):
#     if (s[i] > sr or s[i+1] > sr) and (s[i] + s[i+1]) % 10 == 9:
#         data.append(s[i] + s[i+1])
# print(len(data), min(data))

# s = [int(x) for x in open('17-243.txt')]
# data = []
# maxim = []
# for j in s:
#     if j % 119 == 0:
#         maxim.append(j)
# for i in range(len(s) - 1):
#     if s[i] < max(maxim) and s[i+1] < max(maxim):
#         data.append(s[i] + s[i+1])
# print(len(data), max(data))

# def to8(n):
#     n8 = ''
#     while n:
#         n8 = str(n % 8) + n8
#         n //= 8
#     return n8
#
#
# s = [int(x) for x in open('17-243.txt')]
# data = []
# maxim = []
# for j in s:
#     if j % 127 == 0:
#         maxim.append(j)
# for i in range(len(s) - 1):
#     if (s[i] > max(maxim) or s[i+1] > max(maxim)) and ('31' in str(to8(s[i])) or '31' in str(to8(s[i+1]))):
#         data.append(s[i] + s[i+1])
# print(len(data), min(data))


# s = [int(x) for x in open('17-354.txt')]
# data = []
# k = []
# mini = min(t for t in s if abs(t) % 10 == 1)**2
#
# for i in range(len(s) - 1):
#     k.append(s[i])
#     k.append(s[i+1])
#     if (abs(min(k)) % 10 == 4) and (min(k)**2 + max(k)**2) < mini:
#         data.append(s[i]**2 + s[i+1]**2)
#     k = []
#
# print(len(data), max(data))

# s = [int(x) for x in open('17-354.txt')]
# data = []
# k = []
# mini = min(t for t in s if abs(t) % 10 == 2) ** 2
# for i in range(len(s) - 1):
#     k.append(int(str(s[i])[-1]))
#     k.append(int(str(s[i + 1])[-1]))
#     if max(k) - min(k) == 1 and ((abs(s[i]) % 5 == 0) + (abs(s[i+1]) % 5 == 0)) == 1 \
#             and mini < s[i] ** 2 + s[i + 1] ** 2:
#         data.append(s[i] + s[i+1])
#     k = []
#
# m = []
# for j in data:
#     if j > 0:
#         m.append(j)
# print(len(data), min(m))

# s = [int(x) for x in open('17-370.txt')]
# data = []
# pal = (j for j in s if str(abs(j)) == str(abs(j))[::-1] and 1000 > abs(j) >= 100)
# palindrome = []
# for i in pal:
#     palindrome.append(i)
#
# for i in range(len(s) - 1):
#     if ((len(str(abs(s[i]))) == 4 and len(str(abs(s[i+1]))) != 4) or
#         (len(str(abs(s[i+1]))) == 4 and len(str(abs(s[i]))) != 4)) and \
#             ((s[i] ** 2 + s[i + 1] ** 2) % min(palindrome) == 0):
#         data.append(s[i] ** 2 + s[i + 1] ** 2)
# print(len(data), max(data))

# s = [int(x) for x in open('17-304.txt')]
# even1 = 0
# even2 = 0
# odd1 = 0
# odd2 = 0
# data = []
# maxim = max(s)


# s = [int(x) for x in open('17-1.txt')]
# data = []
# sr = sum(s)/len(s)
# for i in range(len(s) - 2):
#     if (s[i] < sr or s[i + 1] < sr or s[i + 2] < sr) \
#             and ((s[i] % 7 == 0 and s[i+1] % 7 == 0) or (s[i] % 7 == 0 and s[i+2] % 7 == 0) or (s[i+1] % 7 == 0 and s[i+2] % 7 == 0)):
#         data.append(s[i] + s[i + 1] + s[i + 2])
# print(len(data), max(data))

# s = [int(x) for x in open('17-1.txt')]
# data = []
# sr = sum(s)/len(s)
# for i in range(len(s) - 2):
#     if (s[i] < sr or s[i+1] < sr or s[i+2] < sr) and \
#             ((str(s[i]).count('2') >= 1 and str(s[i+1]).count('2') >= 1) or (str(s[i]).count('2') >= 1 and str(s[i+2]).count('2') >= 1) or (str(s[i+1]).count('2') >= 1 and str(s[i+2]).count('2') >= 1)):
#         data.append(s[i] + s[i+1] + s[i+2])
# print(len(data), max(data))

# s = [int(x) for x in open('17-1.txt')]
# data = []
# sr = sum(s)/len(s)
# for i in range(len(s) - 2):
#     if ((s[i] < sr and s[i+1] < sr) or (s[i] < sr and s[i+2] < sr) or (s[i+1] < sr and s[i+2] < sr)) and \
#             (str(s[i]).count('1') >= 1 and str(s[i+1]).count('1') >= 1 and str(s[i+2]).count('1') >= 1):
#         data.append(s[i] + s[i+1] + s[i+2])
# print(len(data), max(data))

# s = [int(x) for x in open('17-380.txt')]
# data = []
# maxi = [j for j in s if str(j)[-2:] == '25']
# maxim = max(maxi)
# for i in range(len(s) - 2):
#     if ((len(str(abs(s[i+2]))) != 4) or (len(str(abs(s[i+1]))) != 4) or (len(str(abs(s[i]))) != 4)) and \
#             (s[i] + s[i+1] + s[i+2] < maxim):
#         data.append(s[i] + s[i+1] + s[i+2])
# print(len(data), max(data))

# s = [int(x) for x in open('17-304.txt')]
# even1 = 0
# even2 = 0
# odd1 = 0
# odd2 = 0
# data = []
# maxim = max(s)

# for i in range(len(s) - 1):
#     for j in str(s[i]):
#         if int(j) % 2 == 0:
#             even1 += 1
#         else:
#             odd1 += 1
#     for j1 in str(s[i + 1]):
#         if int(j1) % 2 == 0:
#             even2 += 1
#         else:
#             odd2 += 1
#     if (s[i] + s[i+1] > maxim) and even1 == odd1 and even2 == odd2:
#         data.append(s[i] + s[i+1])
#     even1 = 0
#     even2 = 0
#     odd1 = 0
#     odd2 = 0
# print(len(data), max(data))
