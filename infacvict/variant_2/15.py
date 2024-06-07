def f(x):
    return (((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (a <= x))

for a in range(1, 10000):
    if all( f(x) for x in range(1, 10000)):
        print(a)
