# Решение Тани
from re import *

f = open('24-334.txt').readline()
r = r'[1-9AB][0-9AB]*[02468A]'
res = findall(r, f)
print(len((max(res, key=len))))
