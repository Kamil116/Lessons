from re import findall

f = open('24_20813.txt')
s = f.readline()

num = '(?:[1-9][0-9]*|0)'
pattern = f'{num}(?:[-*]{num})*'
res = findall(pattern, s)
print(len(max(res, key=len)))
