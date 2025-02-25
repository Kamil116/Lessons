f = open('24-309.txt')
s = f.readline()
s = s.replace('FSRQ', '*')
s = s.split('*')
maxim = 0
for i in range(len(s) - 80):
    maxim = max(sum(map(len, s[i:i + 81])) + 4 * 80 + 6, maxim)
print(maxim)
