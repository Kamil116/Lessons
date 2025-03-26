from re import *

f = open('24-279.txt')
s = f.readline()

pattern = '[1-9A-F][0-9A-F]*'
res = findall(pattern, s)
res = [len(string) for string in res]
print(max(res))
