from re import *

f = open('24-251.txt')
s = f.readline()

pattern = 'A[^AD]*D'
res = findall(pattern, s)
res = [len(string) for string in res]
print(max(res))

pattern = 'D[^AD]*A'
res = findall(pattern, s)
res = [len(string) for string in res]
print(max(res))
