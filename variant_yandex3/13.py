from ipaddress import *

net = ip_network('192.168.76.160/255.255.255.240', 0)
k = 0
res = 0
for i in net:
    print(i)
    k += 1
    s = str(i)[-3:]
    if k % 2 == 0 and s.count('1') % 2 == 0:
        res += 1
print(res)