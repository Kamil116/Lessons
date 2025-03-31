f = open('24.21_19716.txt')
s = f.readline()

cnt = 1
ans = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 1
print(ans)
