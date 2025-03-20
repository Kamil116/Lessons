f = open('24_20909.txt')
s = f.readline()
s = s.split('AB')
maxim = 0
for i in range(len(s) - 100):
    maxim = max(maxim, sum(map(len, s[i:i + 100 + 1])) + 2 + 100 * 2)
print(maxim)
