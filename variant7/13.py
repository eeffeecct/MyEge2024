from ipaddress import *

for x in [255, 254, 252, 248, 240, 224, 198, 128, 0]: 
    net = ip_network(f'51.50.135.169/255.255.255.{x}', 0)
    print(x , net)
