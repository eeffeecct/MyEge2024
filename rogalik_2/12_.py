for x in range(1, 100):
    s = 15 * '7' + 22 * '2' + 22 * '1' + 22 * '4' + 30 * '5' + x * '7' + 10 * '2' + 22 * '1'
    while '72' in s or '27' in s:
        if '1' in s:
            for i in s:
                s = s.replace('1', '', 1)
                if i == '1':
                    s = s.replace('1', '', 1)
                if i != '1':
                    break
