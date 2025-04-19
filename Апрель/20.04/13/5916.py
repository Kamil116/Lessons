from ipaddress import *

for mask in range(33):
    net = ip_network(f'97.122.41.0/{mask}', False)
    if net.network_address == ip_address('97.122.32.0'):
        print(net.netmask)
