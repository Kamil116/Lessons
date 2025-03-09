# Решение Святослава
from ipaddress import *

count = 0
for i in ip_network('172.16.192.0/255.255.192.0'):
    if i.__format__('b').count('1') % 5 != 0:
        count += 1
print(count)
