s = [int(x) for x in open('variant6/171.txt')]
maxim = [i for i in s if i % 50 == 0]
maxi = max(maxim)
data = []
for i in range(len(s) - 2):
    summa1 = s[i] + s[i+1]
    summa2 = s[i+1] + s[i+2]
    summa3 = s[i] + s[i+2]
    m = max(summa1, summa2, summa3)
    if ((str(summa1) == str(summa1)[::-1]) and (str(summa2) == str(summa2)[::-1]) and (str(summa3) == str(summa3)[::-1])) and m < maxi:
        data.append(s[i] + s[i+1] + s[i+2])
print(len(data), max(data))
