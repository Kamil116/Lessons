from re import *

f = open('24-253.txt')
s = f.readline()

# CDACFA
pattern = '(?:[CDF].[AO])+'
res = findall(pattern, s)
print(len(max(res, key=len)) / 3)
