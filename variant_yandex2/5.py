def f(num):
    num_str = str(num)
    if len(num_str) == len(set(num_str)):
        return True
    else:
        return False


for n in range(1000, 10000):
    data = []
    if f(n):
        data.append(str(n).split())
        data.sort()
        sm_max_min = int(data[0][0][0]) + int(data[0][0][3])
        sm_mid = int(data[0][0][1]) * int(data[0][0][2])
        if sm_max_min > sm_mid:
            r = str(sm_mid) + str(sm_max_min)
        else:
            r = str(sm_max_min) + str(sm_mid)
        if int(r) > 85:
            print(n)
            break