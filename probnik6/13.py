from ipaddress import * 
k = 0
net = ip_network(f'34.21.125.12/255.255.192.0', 0)
for ip in net:
    ip_bin = bin(int(ip))[2:].zfill(32)
    if ip_bin[:16].count('1') > ip_bin[16:].count('1'):
        k += 1
print(k)