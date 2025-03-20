f = open('24_12__3b9uf.txt')
s = f.readline()
maxim = 0
cur = 0
for i in range(len(s)):
    # ABCDEFGHIJKLM
    if s[i] in '123456789AABCDEFGHIJKLM':
        cur += 1
        maxim = max(maxim, cur)
    else:
        cur = 0
print(maxim)
