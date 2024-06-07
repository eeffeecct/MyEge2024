s = [int(x) for x in open('kompyand/17komp.txt')]
minim = [x for x in s if str(x)==2 and str(x)[-1] == '7']
for i in range(len(s) - 2):
    chet = (s[i]%2==0) + (s[i+1]%2==0) + (s[i+2]%2==0)
    usl = (s[i]%minim==0) + (s[i+1]%minim==0) + (s[i+2]%minim==0)
    