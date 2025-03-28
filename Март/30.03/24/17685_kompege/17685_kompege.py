from re import *

f = open('24_17685.txt')
s = f.readline()

num = '(?:[1-9][0-9]*|0)'
proizv = rf'(?:{num}\*)*0(?:\*{num})*'
pattern = fr"{proizv}(?:\+{proizv})*"
res = findall(pattern, s)
print(len(max(res, key=len)))
