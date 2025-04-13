f = open('24.txt')
s = f.readline()
ans = 0
for i in range(len(s)):
    letters = digits = 0
    for j in range(i, len(s)):
        if s[j] in 'KLMN':
            letters += 1
        if s[j] in '123':
            digits += 1
        if letters == digits * 2:
            ans = max(ans, j - i + 1)
print(ans)
