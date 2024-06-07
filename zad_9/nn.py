n = [int(x) for x in open('9')]
n9 = [x for x in n if x % 10 == 9]
print(min(n9))