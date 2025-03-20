# Решение Святослава
f = open('24444.txt')
s = f.readline()
# s='===188=1=3=4===138=1=3='

s = s.replace('==', ' ').split()
x = '0123456789'
for x in range(len(s)):
    if s[x][0] == '=':
        s[x] = s[x][1:]
    if s[x][-1] == '=':
        s[x] = s[x][0:-1]
maxim = 0
for x in s:
    if '8' in x.split('='):
        m = len(x)
        if m > maxim:
            maxim = m
    else:
        if '8=' in x:
            maxim = max(maxim, len(x[x.index('8='):len(x)]))

print(maxim)
