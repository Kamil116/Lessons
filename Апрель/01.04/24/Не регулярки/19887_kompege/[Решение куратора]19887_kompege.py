f = open('24.23_19887.txt')
s = f.readline()
cnt = 1
ans = 0
for i in range(len(s) - 1):
    if int(s[i]) % 2 != int(s[i + 1]) % 2:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 1
print(ans)

s = '123456789'
for digit in '0123456789':
    if digit in '13579':
        s = s.replace(digit, '1')
    else:
        s = s.replace(digit, '2')

