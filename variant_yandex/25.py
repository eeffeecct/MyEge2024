from fnmatch import fnmatch

for n in range(42,2 * 10**8 + 1, 42):
    if fnmatch(str(n), '?2*4*0') and fnmatch(str(n), '1*7*') == False:
        print(n, n // 42)
