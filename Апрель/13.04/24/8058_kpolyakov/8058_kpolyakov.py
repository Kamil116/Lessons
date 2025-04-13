# Решение Славы
from re import *

f = open('24-332.txt')
s = f.readline()
pattern = r'[ABC][abc]*(?:\s[ABCabc][abc]*)*\.'
for i in sorted(findall(pattern, s), reverse=1, key=len):
    print(i, len(i))
    break
