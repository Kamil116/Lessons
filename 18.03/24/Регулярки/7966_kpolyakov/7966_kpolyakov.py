# Решение Славы
from re import *

f = open('../files/24-310.txt')
s = f.readline()
nums = '(?:[1-2][0-2]*|0)'
pattern = f'{nums}(?:[+*]{nums})*'
for i in sorted(findall(pattern, s), reverse=True, key=len):
    print(len(i), i)
    input()
"0*1010"
'010*1010+0*0'
