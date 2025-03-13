from re import findall

f = open('24-310.txt')
s = f.readline()

# неотр. число из 3сс *+ неотр. число из 3сс
num = '[1-2][0-2]*|0'
pattern = f'(?:{num})(?:[*+](?:{num})*)'
res = findall(pattern, s)
print(len(max(res, key=len)))
