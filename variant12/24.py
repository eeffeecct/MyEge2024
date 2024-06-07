s = open('variant12/24_11892.txt').readline().split('Y')
k = []
for i in s: 
    if 500 <= i.count('X') <= 505: 
        print(i)
        k.append(len(i))
    
print(min(k))