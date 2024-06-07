def f19(x, y, p):
    if x + y >= 195 and p > 2:
        return p == 2
    if p % 2 != 0:
        return f19(x + 5, y, p + 1) and f19(x, y + 5, p + 1) and f19(x * 3, y, p + 1) and f19(x, y * 3, p + 1)
    else:
        return f19(x + 5, y, p + 1) or f19(x, y + 5, p + 1) or f19(x * 3, y, p + 1) or f19(x, y * 3, p + 1)



# def f20(x, y, p):
#     if x + y >= 195 and p >= 3:
#         return p == 3
#     if p % 2 == 0:
#         return f20(x + 5, y, p + 1) and f20(x, y + 5, p + 1) and f20(x * 3, y, p + 1) and f20(x, y * 3, p + 1)
#     else:
#         return f20(x + 5, y, p + 1) or f20(x, y + 5, p + 1) or f20(x * 3, y, p + 1) or f20(x, y * 3, p + 1)

# def f21(x, y, p):
#     if x + y >= 195 and p >= 2 and p >= 4 :
#         return p == 2 and p == 4
#     if p % 2 != 0:
#         return f21(x + 5, y, p + 1) and f21(x, y + 5, p + 1) and f21(x * 3, y, p + 1) and f21(x, y * 3, p + 1)
#     else:
#         return f21(x + 5, y, p + 1) or f21(x, y + 5, p + 1) or f21(x * 3, y, p + 1) or f21(x, y * 3, p + 1)


print(([i for i in range(1, 184) if f19(11, i, 0)]))
# print(([i for i in range(1, 184) if f20(11, i, 0)]))
# print(([i for i in range(1, 184) if f21(11, i, 0)]))