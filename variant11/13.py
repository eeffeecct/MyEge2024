from ipaddress import *

ip = ip_address('121.74.179.128')
for m in range(33):
    net = ip_network(f'121.74.179.135/{m}', 0)
    if ip == net.network_address:
        print(net.num_addresses)
    # 128