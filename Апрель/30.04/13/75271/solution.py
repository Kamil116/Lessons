from ipaddress import *

minim = 10000
for mask in range(33):
    net_1 = ip_network(f'202.222.47.159/{mask}', 0)
    net_2 = ip_network(f'202.222.47.141/{mask}', 0)
    if net_1.network_address == net_2.network_address:
        if '202.222.47.159' != net_1.network_address.__format__(
                's') and '202.222.47.159' != net_1.broadcast_address.__format__('s'):
            if '202.222.47.141' != net_1.network_address.__format__(
                    's') and '202.222.47.141' != net_1.broadcast_address.__format__('s'):
                minim = min(net_1.num_addresses, minim)
print(minim)
