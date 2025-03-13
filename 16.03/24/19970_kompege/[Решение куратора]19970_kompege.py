from re import findall

f = open('24_19970.txt')
s = f.readline()

# число, кратное 5 * число, кратное 5 * ...
num = '(?:[1-9][1-9]*[05]|0)'
pattern = f'{num}(?:[*+]{num})*'
res = findall(pattern, s)
print(len(max(res, key=len)))
