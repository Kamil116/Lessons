from re import findall

f = open('files/24__13oe8.txt')
s = f.readline()

# AEEEAAAYY
gl = '[AEIOU]*'
res1 = findall(gl, s)
print(len(max(res1, key=len)))

# BBCDHBCH
sogl = '[QWRTPSDFGHJKLZXCVBNMY]*'
res2 = findall(sogl, s)
print(len(max(res2, key=len)))
