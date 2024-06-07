from ipaddress import *

net = ip_network('10.0.4.0/255.255.255.192', 0)
k = 0

for i in list(net)[1:-1]:
    ip_bin = bin(int(i))[2:].zfill(32)
    if '110' not in ip_bin:
        k += 1
print(k)
