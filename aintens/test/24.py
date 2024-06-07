# f = open('aintens/test/24.txt').readline()
# f = f.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0')
# s = ''
# res = []
# for x in f:
#     s += x
#     if '00' in s: 
#         s = s[-1]
#     res.append(len(s))
# print(max(res))


# f = open('aintens/test/24-5.txt').readline()
# s = ''
# data = []
# for x in f:
#     if x in '012345': 
#         s += x
#     else:    
#         try: 
#             while s[0] == '0':
#                 s = s.replace('0','',1)
#         except: 
#             continue
#         data.append(len(s))
#         s = ''
# print(max(data))

# ###################
 
# f = open('aintens/test/24-5.txt').readline()
# f = f.replace('6', ' ')
# f = f.replace('7', ' ')
# f = f.replace('8', ' ')
# f = f.replace('9', ' ')
# print(max(len(s) for s in f.split()))

# f = open('aintens/test/24-6.txt').readline()
# s = ''
# f = f.replace('Y',"X")
# f = f.replace('Z',"X")
# res = []
# for x in f: 
#     s += x
#     if 'XX' in s:
#         s = s[-1]
#     res.append(len(s))
# print(max(res))


# s = open('aintens/test/24-7.txt').readline()
# k = kmax = 1
# for i in range(1, len(s)):
#     if s[i-1] + s[i] in ('RS', 'SQ', 'QR'):
#         k += 1
#         kmax = max(kmax, k)
#     else: 
#         k = 1
# print(kmax)

# s = open('aintens/test/24-8.txt').readline()
# k = 0 # счетчик Y
# kmax = 0 # максим
# l = 0 # левая 
          
# for r in range(len(s)):
#     if s[r] == 'Y': 
#         k += 1
#     while k > 150:
#         if s[l] == 'Y': k -= 1
#         l += 1
#     kmax = max(kmax, r-l+1)
# print(kmax) 

# s = open('aintens/test/24-9.txt').readline()
# k = kmax = 0
# for i in s: 
#     if i in '0123456789ABCDEF':
#         k += 1
#         kmax = max(k, kmax)
#     else: 
#         k = 0
# print(kmax)

s = open('aintens/test/24-10.txt').readline()


