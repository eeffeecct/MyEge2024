n = [int(x) for x in open('17_5292.txt')]
n123 = [x for x in n if x % 123 == 0]
minn123 = min(n123)


summa = []

for i in range(len(n) - 1):
    if (n[i] % 2023 >= minn123) != (n[i+1] % 2023 >= minn123):
        summa.append(n[i] + n[i+1])

print(len(summa), max(summa))