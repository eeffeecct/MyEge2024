from ipaddress import *


net = ip_network('139.75.100.0/255.255.252.0', 0)
for ip in net: 
    ip_bin = bin(int(ip))[2:].zfill(32)

    if ip_bin[24:] == 