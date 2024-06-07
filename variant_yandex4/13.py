from ipaddress import *

net = ip_network('114.179.203.128/255.255.255.192', 0)
k = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 3 == 0: 
        k += 1
print(k)
    