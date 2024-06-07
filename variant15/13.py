from ipaddress import * 

net = ip_network('145.139.8.0/255.255.128.0', 0)
k = 0 
for ip in net: 
    ip_bin = bin(int(ip))[2:].zfill(32)
    if ip_bin[:16].count('1') > ip_bin[16:].count('1') * 3:
        k += 1
print(k)