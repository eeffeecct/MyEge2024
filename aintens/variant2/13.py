from ipaddress import *

for m in range(1,33):
    net = ip_network(f'147.24.128.56/{m}', 0)
    if '147.24.128.0' in str(net):
        print(m)
        break
    