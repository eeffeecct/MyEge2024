s = [int(x) for x in open('aintens/variant2/17.txt')]
sm = [sum(map(int, str(abs(int(x))))) for x in open('aintens/variant2/17.txt')]
data = []
for i in range(len(s) - 2): 
    usl = (len(str(abs(int(s[i])))) == 4) + (len(str(abs(int(s[i+1])))) == 4) + (len(str(abs(int(s[i+2])))) == 4)
    summa = sum(map(int, str(abs(int(s[i]))))) + sum(map(int, str(abs(int(s[i+1]))))) + sum(map(int, str(abs(int(s[i+2])))))
    if usl >= 2 and summa in sm:
        data.append(s[i] + s[i+1] + s[i+2])
print(len(data), max(data))

