from ipaddress import *

for mask in range(0, 33):
    net = ip_network(f'153.202.16.37/{mask}', False)
    if net.network_address == ip_address('153.202.16.32'):
        print(int(str(net.netmask).split('.')[-2]) + int(str(net.netmask).split('.')[-1]))
