from re import findall

f = open('24_21161.txt')
s = f.readline()

pattern = r'[ABC][abc]*(?:\s[ABCabc][abc]*)*\.'
res = findall(pattern, s)
print(len(max(res, key=len)))
