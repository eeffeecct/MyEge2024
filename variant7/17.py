def f(n):
    n13 = ''
    while n:
        n13 = str(n % 13) + n13
        n //= 13
    print(n13)
    return n13

def check3(x, y, z):
    c = 0
    if len(str(x)) == 3:
        c += 1
    if len(str(y)) == 3:
        c += 1
    if len(str(z)) == 3:
        c += 1
    if c == 2:
        return True
    else:
        return False


s =[int(x) for x in open('variant7/17_9872.txt')]
data = []

for i in range(len(s) - 2):
    k = f(abs(max(s[i], s[i+1], s[i+2]))) # троичная
   
    t = check3(abs(s[i]), abs(s[i+1]), abs(s[i+2])) # трехзначное
    if t and (s[i] + s[i+1] + s[i+2]) < int(k) and k[-2:] == '12':
        data.append(s[i]*s[i+1]*s[i+2])
        
print(len(data), max(data))
    


