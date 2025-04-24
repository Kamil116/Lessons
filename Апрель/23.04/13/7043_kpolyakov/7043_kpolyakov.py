from ipaddress import *

maxim = 10000
for A in [255, 254, 252, 248, 240, 224, 192, 128, 0]:
    net = ip_network(f'134.97.250.117/255.255.{A}.0', False)

    flag = True
    for ip in net:
        ip_bin = ip.__format__('b')
        if ip_bin[:16].count('0') < ip_bin[16:].count('0'):
            flag = False
            break
    if flag:
        maxim = min(maxim, A)
print(maxim)
