from ipaddress import *


for m in range(1, 33): 
    net = ip_network(f'175.184.52.103/{m}', 0)
    if '175.184.48.0' in str(net): 
        print(m)