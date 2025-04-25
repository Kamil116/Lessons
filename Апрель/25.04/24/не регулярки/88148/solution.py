f = open('24_M4__42nhn.txt')
s = f.readline()
# s = 'xxxKAZxxxx'
cur = ans = 3
for i in range(3, len(s)):
    if s[i - 3:i] == 'KAZ':
        ans = max(ans, cur)
        cur = 3
    else:
        cur += 1
        ans = max(ans, cur)
print(ans)
