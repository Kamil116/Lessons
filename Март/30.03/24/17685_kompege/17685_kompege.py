from re import *

f = open('24_17685.txt')
s = f.readline()

number = '(?:[1-9][0-9]*|0)'
product = rf'(?:{number}\*)*0(?:\*{number})*'
pattern = rf"{product}(?:\+{product})*"
res = findall(pattern, s)
print(len(max(res, key=len)))
