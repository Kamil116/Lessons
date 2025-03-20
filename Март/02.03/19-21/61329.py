# Решение Святослава
from functools import *


@lru_cache(None)
def f(a, b):
    if a + b > 58:
        return 1
    if 58 >= a + b >= 40:
        return 0
    h = [f(a + 2, b), f(a, b + 2), f(a * 2, b), f(a, b * 2)]
    j = [i for i in h if i <= 0]
    if j:
        return -max(j) + 1
    else:
        return -max(h)


for i in range(1, 32):
    if f(8, i) == -2:
        print(i)
