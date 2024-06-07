from ipaddress import *

net = ip_network('95.112.224.0/255.255.255.128', 0)
k = 0
for i in net:
    ip = bin(int(i))[2:].zfill(32)
    if str(ip[24:32]) == str(ip[24:32])[::-1]:
        k += 1
print(k)