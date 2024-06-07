with open('variant12/27-A_11895.txt') as f:
    n, t, k = [int(x) for x in f.readline().split()] # дни, разница дней, всего руб
    data = [[int(x) for x in s.split()] for s in f] # цена покупки, продажи 

a = 0
for i in range(n): # день покупки
    for j in range(i + t, n): # день продажи
        count = k // data[i][0] # колчество купленных акций 
        viruchka = count * data[j][1] - count*data[i][0] # выручка
        a = max(a, viruchka)
print(a)
 