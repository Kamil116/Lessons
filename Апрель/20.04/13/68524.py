from ipaddress import *

net = ip_network('10.18.134.17/255.255.255.128', False)
print(net.num_addresses - 2)
