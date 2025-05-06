from re import findall

f = open('24-337.txt')
s = f.readline()

num = '[1-9AB][0-9AB]*00'
print(len(max(findall(num, s), key=len)))
