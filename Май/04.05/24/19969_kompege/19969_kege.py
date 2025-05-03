from re import *

s = open('24_19969.txt').readline()
pattern = r'[a-z]+@[a-z]+.[a-z]+'
res = findall(pattern, s)
print(len(max(res, key=len)))
