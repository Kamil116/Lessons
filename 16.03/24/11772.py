from re import *

f = open('files/Задача_8__uhdr.txt')
s = f.readline()
# M, MVM, MVMVM, ...
pattern = 'M(?:VM)*|M(?:DM)*'
res = findall(pattern, s)
print((len(max(res, key=len)) + 1) // 2)
