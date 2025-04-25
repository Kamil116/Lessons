from re import *

f = open('24_2__6jwgo.txt')
s = f.readline()

num = '([789][0789]*)'
pattern = f'{num}([-*]{num})*'

res = findall(pattern, s)
print(str(abs(eval(max(res, key=len))))[:6])
