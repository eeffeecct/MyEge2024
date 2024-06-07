from ipaddress import *


for a in range(0,9):
    k = 0
    net = IPv4Network(f'238.51.1.202/{16+a}',0)
    n = net.num_addresses
    for i in net: 
        ip = bin(int(i))[2:].zfill(32)
        if ip[0:16].count('1') >= ip[16:32].count('1'):
            k += 1
        if k == n:
            print(a)
            break


        