from ipaddress import *

net = ip_network('142.68.56.0/255.255.255.240',0)
k = 0
for i in net:
    ip = bin(int(i))[2:].zfill(32)
    if ip[0:15].count('1') < ip[16:32].count('1'):
        k += 1
print(k)