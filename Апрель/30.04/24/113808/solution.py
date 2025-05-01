from re import *

f = open('24_5__6ao1t.txt')
s = f.readline()

num = '(?:[1-9][0-9]*)'
pattern = f'{num}(?:[*]{num})*'

maxim = 0
for res in findall(pattern, s):
    if eval(res) % 2 == 0:
        maxim = max(maxim, eval(res))
print(str(maxim)[-10:])
