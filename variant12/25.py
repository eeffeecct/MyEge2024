for a in '02468':
    for b in '13579':
        for x in range(133, 10**10, 133):
            if int(str(f'1{a}2357{b}4')) % 133 == 0: 
                print(x, str(f'1{a}2357{b}4') // 133)

for a in '02468':
    for x in range(133, 10**10, 133):
        if int(str(f'1{a}23574')) % 133 == 0: 
            print(x, str(f'1{a}23574') // 133)

# долго работает прога 
        