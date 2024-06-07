from ipaddress import *
k = 0
net = ip_network('145.139.8.0/255.255.128.0', 0)
for i in net: 
    ip = bin(int(i))[2:].zfill(32)
    if ip.count('1') == ip.count('0'):
        k += 1
print(k)
