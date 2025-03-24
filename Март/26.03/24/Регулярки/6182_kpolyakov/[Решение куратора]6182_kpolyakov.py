"""
хитрая задача, потому что нет строгого ограничения,
что А - слева, а D - справа. Может быть не только AxxxD, но и DxxxA
"""
from re import *

f = open('24-251.txt')
s = f.readline()

pattern = 'D[^AD]+A'
res = findall(pattern, s)
print(len(max(res, key=len)))

pattern = 'A[^AD]+D'
res = findall(pattern, s)
print(len(max(res, key=len)))
