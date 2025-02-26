# DB
f = open('7__1vq2i.txt')
s = f.readline()
# s = 'BDBDB'
# DBDB
cur = 0
maxim = -100
for i in range(0, len(s), 2):
    if s[i] == 'D' and s[i + 1] == 'B':
        cur += 1
        maxim = max(maxim, cur)
    else:
        cur = 0
print(maxim * 2, 'DB' * maxim)
# 6DBDBDB
