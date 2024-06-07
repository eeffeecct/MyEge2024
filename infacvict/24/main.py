# s = open('24-157.txt').readline()
# k = kmax = 1
# for i in range(len(s) - 1):
#     if (s[i] != 'R' or s[i+1] != 'P') and (s[i] != 'P' or s[i+1] != 'R'):
#         k += 1
#         kmax = max(kmax, k)
#     else:
#         k = 1
# print(kmax)

# s = open('k7a-4.txt').readline()
# k = kmax = 0
# for i in range(len(s)):
#     if s[i] != 'D':
#         k += 1
#         kmax = max(kmax, k)
#     else:
#         k = 0
# print(kmax)

# s = open('k7a-3.txt').readline()
# k = kmax = 0
# for i in range(len(s)):
#     if s[i] in 'ABEF':
#         k += 1
#         kmax = max(kmax, k)
#     else:
#         k = 0
# print(kmax)

# s = open('24-1.txt').readline()
# k = kmax = 1
# for i in range(len(s) - 1):
#     if s[i] < s[i+1]:
#         k += 1
#         if k > kmax:
#             kmax = k
#             pos = i+1
#         kmax = max(kmax, k)
#     else:
#         k = 1
# print(s[pos-kmax+1:pos+1], kmax)

# s = '.' + open('24-181.txt').readline() + '.'
# kmax = 0
# data = [i for i in range(len(s)) if s[i] == '.']    # генерируем индексы где стоят точки
# for i in range(len(data) - 5):
#     kmax = max(kmax, data[i + 5] - data[i] - 1)     # находим расстояние, между точками находится <= 4 точек
# print(kmax)

# kmin = 999999
# s = open('24-263.txt').readline()
# data = [i for i in range(len(s)) if s[i] == 'Z']
# for i in range(len(data) - 119):
#     kmin = min(kmin, data[i + 119] - data[i] + 1)
# print(kmin)

# s = open('24-1.txt').readline()
# for c in 'ABX':
#     s = s.replace(c, '*')
# s = '*' + s + '*'
# a = [i for i in range(len(s)) if s[i] == '*']
# print(max(a[i+6] - a[i] - 1 for i in range(len(a) - 6)))

# s = open('infacvict/24/24-181.txt').readline().split('Y') # большой массив разделенный Y
# m = 0
# for ss in s:
#     ss = ss.split('.') # разбили по . (['LLOLTMS', 'EWKGAQVEEJWDPIWNM', 'PHBLQ', 'AWO'])
#     print(ss)
#     lens = [len(''.join(ss[i:i+6])) for i in range(len(ss))]
#     m = max(m, max(lens) + 5)
# print(m)

# s = open('24-181.txt').readline()
# kmax = 0
# for p in s.split('.'):
#     if p.count('A') >= 3:
#         kmax = max(kmax, len(p))
# print(kmax)

# s = open('infacvict/24/24-191.txt').readline().split('A')
# k=0
# for i in s[1:-1]:
#     if 'B' not in i and len(i) >= 15:
#         k += 1
# print(k)

# s = open('infacvict/24/24-191.txt').readline()
# s = s.replace('A', '*A').replace('B', 'B*').split('*')
# k = 0
# for i in s:
#     if len(i) <= 15 and i.count('A') == 1 and i.count('B') == 1 and 'F' in i:
#         k += 1
# print(k)

# s = open('infacvict/24/24-197.txt').readline()
# k = kmax = 0
# for j in range(3):
#     k = 0
#     for i in range(j, len(s) - 2, 3):
#         if s[i:i+3] in ('XXX', 'XYX', 'XZX', 'YXY', 'YYY', 'YZY'): 
#             k += 1
#             kmax = max(kmax, k)
#         else: 
#             k = 0
# print(kmax)

# s = open('infacvict/24/24-210.txt').readline()
# k = kmax = 0
# i = 0
# s = 'BDEABCBABCABBD'
# while i < len(s) - 2:
#     if s[i:i+3] in ('ABC', 'BAC', 'CAB', 'CBA'):
#         k += 1
#         kmax = max(kmax, k)
#         i += 1 # перескок 
#     else:
#         k = 0
#     i += 1
# print(kmax)

# s = open('infacvict/24/24-241.txt').readline()
# kmax = k = 0
# i = 0
# while i < len(s) - 2:
#     if s[i] in 'BCDF' and s[i+1] in 'BCDF' and s[i+2] in 'AEO':
#         k += 1
#         kmax = max(kmax, k)
#         i += 3
#     else:
#         k = 0
#         i += 1
# print(kmax)

# s = open('infacvict/24/24-215.txt').readline()
# i = 0
# kmax = k = 0
# while i < len(s) - 2:
#     if s[i] in '123' and s[i+1] in 'ABC' and s[i+2] in '123': 
#         k += 1
#         kmax = max(k, kmax)   
#         i += 3
#     else:
#         k = 0
#         i += 1
# print(kmax)

# s = open('infacvict/24/24-264.txt').readline()
# kmax = k = 0
# p = ''
# for i in s:
#     if i in '0123456789':
#         p += 'X'
#     else:
#         p += 'Y'
# for j in range(0, len(p) - 1, 2): 
#     if p[j] != p[j+1]:
#         k += 1
#         kmax = max(kmax, k)
#     else:
#         k = 0
# print(kmax)

# def count_letters(arr):
#     letter_counts = {}
#     for letter in arr:
#         if letter in letter_counts:
#             letter_counts[letter] += 1
#         else:
#             letter_counts[letter] = 1
#     return letter_counts
# s = open('infacvict/24/24-s2.txt').readline().split('A')
# data = []
# for i in range(len(s)): 
#     if len(s[i]) != 0:
#         data.append(s[i][0])
# print(count_letters(data)) 

# def count_letters(arr):
#     letter_counts = {}
#     for letter in arr:
#         if letter in letter_counts:
#             letter_counts[letter] += 1
#         else:
#             letter_counts[letter] = 1
#     return letter_counts
# s = open('infacvict/24/24-s2.txt').readline().split('A')
# data = []
# for i in s:
#     try:
#         if i[1] == 'C':
#             data.append(i[0])
#     except:
#         pass 
# print(count_letters(data))

# k = 0
# for s in open('infacvict/24/24-s1.txt'):
#     if s.count('K') > s.count('U'):
#         k += 1
# print(k)

# k = 0
# for s in open('infacvict/24/24-s1.txt'):
#     for i in range(len(s) - 2):
#         if s[i] == 'F' and s[i+2] == 'O':
#             k += 1
#             break
# print(k)

# s = 'lskjdhfgsdf'
# print(s.index('f'), s.rindex('f'))

# maxim = 0
# for s in open('infacvict/24/24-164.txt'):
#     if s.count('E') < 20:
#         for i in s:
#             maxim = max(maxim, s.rindex(i) - s.index(i))
# print(maxim)

