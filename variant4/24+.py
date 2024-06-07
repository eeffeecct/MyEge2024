f = open('24_6636.txt')
w = f.readline()
w = w.replace('3', '1')
w = w.replace('5', '1')
w = w.replace('4', '2')
w = w.replace('21', '*')
k = 0
maxi = 0
for i in range(len(w)):
    if w[i] == '*':
        k += 1
    else:
        maxi = max(maxi, k)
        k = 0
print(maxi)
