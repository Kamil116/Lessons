from re import *

f = open('24-279.txt')
s = f.readline()

num = '[1-9A-F][0-9A-F]*'
res = findall(num, s)
print(len(max(res, key=len)))
