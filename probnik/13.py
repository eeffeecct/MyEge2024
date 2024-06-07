from ipaddress import *
k = 0
net = ip_network('192.168.133.192/255.255.255.192', 0)
for i in net:
    s = bin(int(i))[2:]
    if s.count('1') % 3 != 0:
        k += 1
print(k)
