for n in range(3, 10001):
    s = '8' + n*'4'
    while '4444' in s or '844' in s or '84' in s:
        if '4444' in s:
            s = s.replace('4444', '884', 1)
        elif '844' in s:
            s = s.replace('844', '488', 1)
        elif '84' in s:
            s = s.replace('84', '3343', 1)
    if len(s) >= 20:
        print(n)
        break
