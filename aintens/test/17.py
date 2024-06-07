# s = [int(x) for x in open('aintens/test/17.txt')]
# maxim = max([x for x in s if abs(x) % 100 == 21 and len(str(abs(x))) == 5])
# data = []
# for i in range(len(s) - 1): 
#     usl = (abs(s[i])%100==21 and len(str(abs(s[i])))==5) + (abs(s[i+1])%100==21 and len(str(abs(s[i+1])))==5)
#     summa = s[i]**2 + s[i+1]**2
#     if usl == 1 and summa >= maxim**2:
#         data.append(s[i] + s[i+1])
# print(len(data), max(data))

# s = [int(x) for x in open('aintens/test/17-1.txt')]
# minim = min([x for x in s if x % 19 == 0])
# data = []
# for i in range(len(s) - 1): 
#     usl = (s[i] % minim == 0) + (s[i+1] % minim == 0)
#     if usl >= 1:
#         data.append(s[i] + s[i+1])
# print(len(data), max(data))


# s = [int(x) for x in open('aintens/test/17-2.txt')]
# maxim = max([x for x in s if len(str(abs(int(x)))) == 4 and str(abs(int(x)))[-2:] == '39'])**2 # 9239
# data = []
# for i in range(len(s) - 1):
#     usl = (len(str(abs(int(s[i])))) == 4) + (len(str(abs(int(s[i+1])))) == 4)
#     summa_kv = (s[i] + s[i+1])**2
#     if usl == 1 and summa_kv <= maxim:
#         data.append(s[i] + s[i+1])
# print(len(data), max(data))

# s = [int(x) for x in open('aintens/test/17-3.txt')]
# maxim = max([x for x in s if str(x)[-1] == '3'])**2
# data = []
# for i in range(len(s) - 1):
#     usl = (str(s[i])[-1] == '3') + (str(s[i+1])[-1] == '3')
#     summa_kv = s[i]**2 + s[i+1]**2
#     if usl == 1 and summa_kv >= maxim:
#         data.append(summa_kv)
# print(len(data), max(data))

s = [int(x) for x in open('aintens/test/17-4.txt')]
maxim = max([x for x in s if str(x)[-2:] == '15'])
data = []
for i in range(len(s) - 2):
    usl = (len(str(s[i])) == 4) + (len(str(s[i+1])) == 4) + (len(str(s[i+2])) == 4)
    summa = s[i] + s[i+1] + s[i+2]
    if usl == 1 and summa >= maxim:
        data.append(summa)
print(len(data), max(data))