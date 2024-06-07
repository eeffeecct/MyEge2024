from ipaddress import *

for m in range(1,33): 
    net = ip_network(f'127.220.170.23/{m}', 0)
    if '127.220.168.0' in str(net):
        print(m)
        break