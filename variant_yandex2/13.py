from ipaddress import *
k = 0
net = ip_network('212.192.32.118/255.255.255.224', 0)
for i in net:
    s = bin(int(i))[2:]
    if (s[-1] != '1' and s[-2] != '1' and s[-3] != '1') or (s[-1] != '0' and s[-2] != '0' and s[-3] != '0'):
        k += 1
print(k)
