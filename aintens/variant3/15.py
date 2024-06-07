for a in range(1, 1000): 
    if all((x % a != 0) <=( (x % 14 == 0) <= (x % 4 != 0) )for x in range(1, 1000)):
        print(a)