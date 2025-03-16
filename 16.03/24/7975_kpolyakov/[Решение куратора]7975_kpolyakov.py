from re import *

f = open('../files/24-314.txt')
s = f.readline()

# неотр. число *+ число *+ число ...
num = '(?:[1-9][0-9]*|0)'
pattern = f'{num}(?:[*+]{num})*'
res = findall(pattern, s)
print(eval(max(res, key=len)))
