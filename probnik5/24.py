s = open('probnik5/24.txt').readline()
# k = kmax = 0
# for i in range(0, len(s) - 4, 4):
#     if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C' and s[i+3] == 'D':
#         k += 1
#     else: 
#         kmax = max(k, kmax)
#         k = 0
# print(kmax)
s1 = 61*'ABCD' + 'ABCD'

if s1 in s: 
    print('true')
else: 
    print('False')
