s = open('kompyand/24.txt').readline()
e = 0
k = 0
data = []
for i in range(len(s) ):
    if s[i] == 'E': 
        e = 1
        for j in range(i+1, len(s)):
            if s[j] == 'E':
                e += 1
            
            if e == 240: 
                data.append(j-i+1)
                break
print(min(data))
    
    