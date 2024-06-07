from ipaddress import *

net = ip_network('192.168.32.160/255.255.255.240', 0)
k = 0
for ip in net:
    ip_bin = bin(int(ip))[2:].zfill(32)
    if ip_bin.count('1') % 2 == 0:
        k += 1
print(k)