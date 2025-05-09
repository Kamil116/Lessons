from re import findall

f = open('24-337.txt')
s = f.readline()
num = '1[0-9ABCD]*0'
pattern = f'{num}'
print(len(max(findall(pattern, s), key=len)))
