from ipaddress import * 
data = set()
for a in range(256):
    net = ip_network(f'191.51.{a}.13/255.255.254.0', 0)
    for ip in net: 
        ip_bin = bin(int(ip))[2:].zfill(32)
        if ip_bin[:16].count('1') > ip_bin[16:].count('1'):
            data.add(a)
print(len(data))
