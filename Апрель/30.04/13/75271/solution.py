from ipaddress import *

for mask in range(33):
    net_1 = ip_network(f'202.222.47.159/{mask}', False)
    net_2 = ip_network(f'202.222.47.141/{mask}', False)
    if '202.222.47.159' != net_1.network_address.__format__(
            's') and '202.222.47.159' != net_1.broadcast_address.__format__('s'):
        if '202.222.47.141' != net_1.network_address.__format__(
                's') and '202.222.47.141' != net_1.broadcast_address.__format__('s'):
            print(net_1.num_addresses)
