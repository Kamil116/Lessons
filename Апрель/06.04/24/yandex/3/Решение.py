# Решение Амины
f = open('24.txt')
s = f.readline()
num = ''
mx = 0
for i in range(len(s)):
    if s[i] in '0123456789':
        num += s[i]
        if int(num) > mx:
            mx = int(num)
    else:
        num = ''
print(mx)
