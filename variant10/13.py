from ipaddress import *

for m in range(1, 33):
    net = ip_network(f'111.81.27.224/{m}', 0 )
    if '111.81.27.192' in str(net):
        print(net.netmask)

