s = [int(x) for x in open('17.txt')]
maxi = [i for i in s if str(i)[-3:] == '221']
data = []
for i in range(len(s)-2):
    if (( (abs(s[i]) >= 10 and int(str(s[i])[-2]) % 2 != 0) and (abs(s[i+1]) >= 10 and int(str(s[i+1])[-2]) % 2 != 0) and abs(s[i+2]) <= 9) or \
    ( (abs(s[i]) >= 10 and int(str(s[i])[-2]) % 2 != 0) and (abs(s[i+1]) <= 9) and (abs(s[i+2]) >= 10 and int(str(s[i+2])[-2]) % 2 != 0)) or \
    ( (abs(s[i]) <= 9) and (abs(s[i+1]) >= 10 and int(str(s[i+1])[-2]) % 2 != 0) and (abs(s[i+2]) >= 10 and int(str(s[i+2])[-2]) % 2 != 0))) and \
    ((abs(s[i]) <= 9 or abs(s[i]) >= 100) or (abs(s[i+1]) <= 9 or abs(s[i+1]) >= 100) or (abs(s[i+2]) <= 9 or abs(s[i+2]) >= 100)) and \
    (s[i] + s[i+1] + s[i+2] > max(maxi)):
        data.append(s[i] + s[i+1] + s[i+2])
print(len(data), min(data))
