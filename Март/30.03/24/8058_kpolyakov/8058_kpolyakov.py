from re import *

f = open('24-332.txt')
s = f.readline()

pattern = r'[ABC][a-z]*(?:\s[ABCabc][abc]*)*\.'
res = findall(pattern, s)
print(len(max(res, key=len)))
