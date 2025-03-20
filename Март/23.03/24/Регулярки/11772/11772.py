from re import *

f = open('../files/Задача_8__uhdr.txt')
s = f.readline()
s = 'AEBCADDE'

pattern = 'M(?:[VD]M)+'
result = findall(pattern, s)
print(result)
