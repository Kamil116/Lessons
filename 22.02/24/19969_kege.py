# Решение Тани
from re import *

s = open('444').readline()
a = []
pattern = r'[a-z]+@[a-z]+.[a-z]+'
for i in (findall(pattern, s)):
    a.append(len(i))
print(max(a))
