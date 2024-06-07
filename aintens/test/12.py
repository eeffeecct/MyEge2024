for n in range(0, 100):
    s = '1'*n + '2'*n + '3'*n
    print(s)
    while '21' in s or '31' in s or '32' in s: 
        s = s.replace('21','12',1)
        s = s.replace('31','13',1)
        s = s.replace('32','23',1)
   
    if s.count('1') == s.count('2') == s.count('3') and len(s) >= 50 and s[49] == '2':
        print(n*3)
        break
    