# Решение Тани
s = open('24_20909.txt').readline()
s = s.replace('AB', 'A B').split()
mx = 0
for i in range(len(s) - 100):
    r = ''.join(s[i:i + 101])
    mx = max(mx, len(r))
print(mx)

