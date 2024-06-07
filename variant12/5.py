for n in range(100, 1000):
    s = ''
    s1 = int(str(n)[0])*int(str(n)[1])
    s2 = int(str(n)[1])*int(str(n)[2])
    if s1 > s2: 
        s = str(s2) + str(s1)
    else: 
        s = str(s1) + str(s2)
    if int(s) == 621: 
        print(n)