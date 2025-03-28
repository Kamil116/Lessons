from re import *

f = open('24-2__63h4e.txt')
s = f.readline()

num = '[1-4]+'
pattern = fr'A{num}(?:[+*]{num})*'
res = findall(pattern, s)
print(len(max(res, key=len)))
