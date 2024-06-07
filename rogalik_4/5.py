# def f(n):
#     n5 = ''
#     while n:
#         n5 = str(n % 5) + n5
#         n //= 5
#     return n5

# def check_same_digits(num):
#     num_str = str(num)
#     first_digit = num_str[0]
#     for digit in num_str:
#         if digit != first_digit:
#             return False
#     return True


# for n in range(1,1000):
#     s = f(n)
#     if s[0]!='0' and ((s.count('0')+s.count('2')+s.count('4')) > (s.count('1')+s.count('3'))):
#         s += '42'
#     elif s[0]!='0' and ((s.count('0')+s.count('2')+s.count('4')) <= (s.count('1')+s.count('3'))):
#         s += '31'
#     if check_same_digits(int(s,5)):
#         print(n)
#         print(int(s,5))
#         break

def f(n):
    n5 = ''
    while n:
        n5 = str(n % 5) + n5
        n //= 5
    return n5


for n in range(10,137):
    s = f(n)
    if int(s[-2]) > int(s[-1]):
        s = s[:-2] + s[-1] + s[-2]
    elif int(s[-2]) < int(s[-1]):
        s = s[1] + s[0] + s[2:]
    s = int(s,5)
    if len(str(s)) == 3:

        print(n)

