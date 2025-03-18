from re import *

f = open('../files/Задача_7__uhdq.txt')
s = f.readline()
# M, MM, MMM, ...
pattern = 'M*'
res = findall(pattern, s)
print(len(max(res, key=len)))
