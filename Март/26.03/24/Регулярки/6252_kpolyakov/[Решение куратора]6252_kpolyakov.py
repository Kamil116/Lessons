from re import *

f = open('24-253.txt')
s = f.readline()

pattern = '(?:[CDF][A-Z][AO])+'
res = findall(pattern, s)
print(len(max(res)))
