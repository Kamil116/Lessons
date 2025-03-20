from re import *

f = open('../files/Задача_7__uhdq.txt')
s = f.readline()

pattern = 'M+'

max_len = 0
for result in findall(pattern, s):
    max_len = max(len(result), max_len)
# print(max_len)

print(max([len(i) for i in findall(pattern, s)]))
# print(max(map(len, findall(pattern, s))))
