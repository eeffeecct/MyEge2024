s = [int(x) for x in open('variant16/17-382.txt')]
minim = min([x for x in s if x % 100 == 11])

for i in range(len(s) - 1):
    usl = (len(str(s[i])) != 3) + (len(str(s[i+1])) != 3)
    # отличаются на значение? 
    