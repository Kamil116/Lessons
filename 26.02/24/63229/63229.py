f = open('5__1vf5z.txt')
s = f.readline()
s = s.replace('C', '*')
# DDD*AAAAA* -> ['DDD', 'AAAA']
s = s.split('*')
maxim = -10000
for x in s:
    maxim = max(len(x), maxim)
print(maxim)
