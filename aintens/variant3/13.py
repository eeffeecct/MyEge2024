from ipaddress import *

net = ip_network('122.159.136.144/255.255.255.248', 0)
k = 0
for ip in net: 
    ip_bin = bin(int(ip))[2:].zfill(32)
    if ip_bin.count('1') % 4 != 0:
        k += 1
print(k)