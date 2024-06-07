for i in range(1, 110):
    s = bin(i)[2:].zfill(8)    
    s = s[:2] + s[-2:]
    if int(s, 2) == 7:
        print(i)
         
