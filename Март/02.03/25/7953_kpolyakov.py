# Решение Святослава
from fnmatch import *


def f(n):
    if len(str(n)) % 2 == 0:
        g = (len(str(n)) // 2)
        h = str(n)[0:g]
        h1 = str(n)[g:]
        h2 = (int(h) + int(h1)) ** 2
        if h2 == n:
            return 1
        else:
            return 0


for i in range(0, 35 * 10 ** 6 + 1):
    if i % 25 == 0 and f(i) == 1:
        if fnmatch(str(i), '*2*0*2*5*'):
            print(i, i // 25)
