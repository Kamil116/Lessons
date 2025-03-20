from ipaddress import *

for mask in range(0, 33):
    net = ip_network(f'143.131.211.37/{mask}', False)

    cnt = 0
    for ip in net:
        ip_bin = ip.__format__('b')
        if ip_bin.count('1') == 10:
            cnt += 1
        if cnt > 15:
            break
    if cnt == 15:
        print(net.netmask.__format__('b').count('1'))

