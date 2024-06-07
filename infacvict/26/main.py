# data = open('infacvict/26/26-5.txt').readlines() # все строки из файла
# s, _ = map(int, data[0].split())    # первую строку в файле добавили в массив и режем
# del data[0]
# data = sorted(int(i) for i in data)
# total = 0   # сколько уже накоплено

# for i, val in enumerate(data): # i - счетчик, val - значение / i начинается с 0
#     if total + val > s: break   # останавливаем если след добавление будет перебор
#     total += val
# print(i)
# files = [x for x in data if (x - data[i-1]) <= (s - total)]     # если ( текущ вес файла - data[i-1] ) <= Максимум возможного - сколько сейчас всего
# print(max(files))

with open('infacvict/26/26-101.txt') as f: 
    n, k = map(int, f.readline().split())
    s = []
    for i in f: 
        s.append([int(i)])
    s.sort(reverse=True)

print(s)
count = 1
while data: 
    if data[]
