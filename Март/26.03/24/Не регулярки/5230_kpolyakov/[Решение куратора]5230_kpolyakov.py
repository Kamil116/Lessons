f = open('24-1.txt')
s = f.readline()
left = 0
maxim = 0
gl_count = 0
for right in range(len(s)):
    if s[right] in 'AEIOUY':
        gl_count += 1
    while gl_count == 6:
        maxim = max(maxim, right - left)
        if s[left] in 'AEIOUY':
            gl_count -= 1
        left += 1

print(maxim)
