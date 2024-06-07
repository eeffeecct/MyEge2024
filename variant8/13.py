from ipaddress import *

net = ip_network(f'192.168.32.128/255.255.255.192', 0)
k = 0
for ip in net:
    ip_bin = bin(int(ip))[2:].zfill(32)
    if ip_bin.count('1') % 2 == 0:
        k += 1
print(k)
