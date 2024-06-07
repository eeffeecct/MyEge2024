# 1. всевозможные пары
# 2. всевозможные тройки
# 3. всевозможные тройки на раст. не менее K
# 4. нахождение непрерывных последовательностей

# li = [10,27,80,91,56]
# K = 100
# N = 5
# c = 0
# for i in range(0, N-1):
#     for j in range(i + 1, N):  # справа от текущ 
#         if li[i] + li[j] >= K: # текущ + след
#             c += 1
# print(c)


# n = [1, 3, 2, 5, 6, 41]
# res = []
# k = 2
# for i in range(0, len(n)):  # left
#     for j in range(i + k, len(n)):  # mid если отстает от к
#         for g in range(j + k, len(n)):  # right если отстает от к
#             res.append(n[i] + n[j] + n[g])
# print(res)

# n = [1, 3, 2, 5, 6, 41]
# res = []
# for i in range(0, len(n)):
#     seq = []
#     for j in range(i, len(n)):
#         seq.append(n[j])
#
#         res.append(sum(seq))
# print(res)
# макс сумм подпоследовательности


# n = [1, 3, 2, 5, 6, 41]
# res = []
# k = 2
# for i in range(0, len(n)):  # left
#     for j in range(i + k, len(n)):  # mid если отстает от к
#         for g in range(j + k, len(n)):  # right если отстает от к
#             res.append(n[i] + n[j] + n[g])
# print(res)



