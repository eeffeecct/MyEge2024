from fnmatch import fnmatch

for n in range(5716, 10**10, 5716):
    if fnmatch(str(n), '56*139?4'):
        print(n, n // 5716)

# otvet: 
# 5638513904 986444
# 5638713964 986479
# 5686213924 994789
# 5686413984 994824
