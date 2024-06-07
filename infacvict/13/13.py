# адрес сети бывает с маской
#
from ipaddress import *

# for m in range(1,33):
#     net = ip_network(f'111.81.200.27/{m}', 0)
#     if '111.81.192.0' in str(net):
#         print(net.netmask)

# for m in range(1,33):
#     net = ip_network(f'190.120.251.78/{m}', 0)
#     if '190.120.251.0' in str(net):
#         print(32-m)

# for m in range(33):
#     net1 = ip_network(f'11.156.152.142/{m}', 0)
#     net2 = ip_network(f'11.156.157.39/{m}', 0)
#     if net1 == net2:
#         print(str(net1.netmask)[8:11])

# k = 0
# net = ip_network(f'184.178.54.144/255.255.255.240', 0)
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if '111' in ip_bin:
#         k += 1
# print(k)

# k = 0
# net = ip_network(f'192.168.32.160/255.255.255.240', 0)
# for i in net:
#     ip_bin = bin(int(i))[2:]
#     if ip_bin.count('1') % 2 == 0:
#         k += 1
# print(k)


# data = []
# net = ip_network(f'124.8.0.0/255.248.0.0', 0)
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)
#     data.append(ip_bin.count('0'))
# print(max(data))

# for m in range(33):
#     net = ip_network(f'108.133.75.91/{m}', 0)
#     if '108.133.75.64' in str(net):
#         print(net, net.num_addresses)
# k = 0
# net = ip_network(f'186.135.80.0/255.255.252.0', 0)
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)
#     if ip_bin[:16].count('1') > ip_bin[16:].count('1'):
#         k += 1
# print(k)


k = 0
net = ip_network(f'249.0.33.87/255.252.0.0', 0)
for ip in net:
    ip_bin = bin(int(ip))[2:].zfill(32)
    if (ip_bin[:16].count('1') * 2) < ip_bin[16:].count('1'):
        k += 1
print(k)


























