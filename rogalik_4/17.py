def check_same_digits(num):
    num_str = str(num)
    first_digit = num_str[0]
    for digit in num_str:
        if digit != first_digit:
            return False
    return True


data = []
s = [int(i) for i in open('17_1.txt')]
maxi = [j for j in s if check_same_digits(j) and len(str(abs(j))) == 3]
maxim = max(maxi)

for i in range(len(s) - 1):
    if ((len(str(abs(s[i]))) == 2 and len(str(abs(s[i+1]))) != 2 and str(abs(s[i]))[0] == str(abs(s[i]))[1]) or \
        (len(str(abs(s[i+1]))) == 2 and len(str(abs(s[i]))) != 2 and str(abs(s[i+1]))[0] == str(abs(s[i+1]))[1])) and \
        (s[i] + s[i+1] <= maxim):
        data.append(s[i]**2 + s[i+1]**2)
print(len(data), max(data))
