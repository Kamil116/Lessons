from ipaddress import *

net = ip_network('134.127.52.160/255.255.255.224')
ans = 0
for ip in net:
    if ip.__format__('b').count('1') % 2 == 0:
        ans += 1
print(ans)
