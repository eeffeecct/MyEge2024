from ipaddress import * 

net = ip_network('192.168.32.48/255.255.255.240',0)
k = 0
for ip in net: 
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 2 != 0:
        k += 1
print(k)