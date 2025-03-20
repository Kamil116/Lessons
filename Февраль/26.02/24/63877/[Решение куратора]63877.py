f = open('7__1vq2i.txt')
s = f.readline()
cur, maxim = 0, 0
for start in range(2):
    for i in range(start, len(s) - 1, 2):
        if s[i] + s[i + 1] == 'DB':
            cur += 1
            maxim = max(cur, maxim)
        else:
            cur = 0
print(maxim * 2, 'DB' * maxim, sep='')
