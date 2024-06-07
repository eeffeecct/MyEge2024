# from ipaddress import *
#
# net = ip_network('235.86.56.0/255.255.248.0', 0)
#
# k = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if '11' in ip_bin[-2:]:
#         k += 1
# print(k) # 512
#

# from ipaddress import *
# for x in range(1, 33):
#     net = ip_network(f'192.75.64.98/{x}', 0)
#     if net.network_address == ip_address('192.75.64.0'):
#         print(x)
#
#
# from ipaddress import *
#
# for x in range(1, 33):
#     net = ip_network(f'118.187.59.255/{x}', 0)
#     net2 = ip_network(f'118.187.65.115/{x}', 0)
#     if net.network_address != net2.network_address:
#         if IPv4Address('118.187.59.255') not in [net.network_address, net.broadcast_address]:
#             if IPv4Address('118.187.65.115') not in [net2.network_address, net2.broadcast_address]:
#                 print(x)
#
#from ipaddress import *
#for x in range(1, 9):
#    net = ip_network(f'112.117.107.70/{x+16}', 0)
#    net2 = ip_network(f'112.117.121.80/{x+16}', 0)
#    if net.network_address == net2.network_address:
#        print(net.netmask.packed[2])


from ipaddress import *
for x in range(1, 256):
    net = ip_network(f'183.192.{x}.0', 0)
    if net.network_address == net2.network_address:
        print(net.netmask.packed[2])
