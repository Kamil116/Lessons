from re import *

f = open('../files/Задача_7__uhdq.txt')
s = f.readline()
# s = 'MMMVMVM'

pattern = 'M+'
print(max(findall(pattern, s), key=len))

maxim = 0
for result in finditer(pattern, s):
    maxim = max(maxim, len(result.group()))
print(maxim)
