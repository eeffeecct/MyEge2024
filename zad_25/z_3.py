from fnmatch import fnmatch

for n in range(237, 10**8, 237):
    if fnmatch(str(n), '81?2*[0-8]80'):
        print(n, n // 237)

# otvet:
# 8162280 34440
# 81229380 342740
# 81324180 343140
# 81727080 344840
# 81821880 345240
