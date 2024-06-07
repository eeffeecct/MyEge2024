# 1. неравенство
# 2. делители
# 3. отрезки
# 4. поразрядная &

# for a in range(0, 1000):
#     res = True
#     for x in range(0, 100):
#         for y in range(0, 100):
#             f = (x + 2*y < a) or (y > x) or (x > 60)
#             if f == False:
#                 res = False
#     if res == True:
#         print(a)
#         break

# for a in range(0, 1000):
#     if all(((x * y < a) or (x < y) or (9 < x)) for x in range(0, 1000) for y in range(0, 1000)):
#         print(a)
#         break # 82

# for a in range(0, 1000):
#     if all(((x + y <= a) or (y > 150) or (x + 3*y > 600)) for x in range(0, 1000) for y in range(0, 1000)):
#         print(a)
#         break

# for a in range(1, 1000):
#     if all(( ((x % 3 == 0) <= (x % 2 != 0)) or (x - a >= 4)) for x in range(1, 1000)):
#         print(a)
#         break

# def f(a, x):
#     return ((x % 3 == 0) <= (x % 2 != 0)) or (x - a >= 4)

# for a in range(1, 1000):
#     if all(f(a,x) for x in range(1, 1000)):
#         print(a)


# for a in range(0,1000):
#     if all((x)):
#         print(a)
#         break

# for a in range(1, 1000):
#     if all(( (x != a) <= ) for x in range(1, 1000)):
#         print(a)
#         break


# на множества 

# p = {1,3,4,9,11,13,15,17,19,21}
# q = set(range(3, 31, 3))
# a = set()
# for x in range(1, 1000):
#     if not(((x in p) <= (x in a)) or ((x not in a) <= (x not in q))):
#         a.add(x)
# a = list(a)
# data = 1
# for i in range(len(a)):
#     data = data * a[i]
# print(data)


# p = set(range(2, 21, 2))
# q = set(range(5, 51, 5))
# a = set(range(1, 1000))
# for x in range(1, 1000):
#     if not(((x in a) <= (x in p)) and ((x in q) <= (x not in a))):
#         a.remove(x)
# print(len(a))














