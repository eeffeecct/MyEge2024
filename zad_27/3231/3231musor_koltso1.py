f = open('zad_27/3231/27-A_3231.txt')
N = int(f.readline())
trash = [int(x) for x in f]
for i in range(N):
    s = 0
    for j in range(N):
        s += min(abs(j-i), N - abs(j-i)) * trash[j]
    print(i + 1, s)
