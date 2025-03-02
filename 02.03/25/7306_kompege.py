# Решение Полины
from fnmatch import *


def f(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 or n == 1:
            return 0
    else:
        return 1 and n != 1


d = []
for n in range(1, 10 ** 5):
    if f(n) == 1:
        d.append(n)

for i in range(len(d)):
    if f(i + 1) == 1:
        if fnmatch(str(d[i]), '1*7?7'):
            print(d[i], i + 1)
