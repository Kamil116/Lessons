f = open('24_16__3b9u2.txt')
s = f.readline()
s = s.split('Y')
minim = 10000
for i in range(len(s) - 99):
    minim = min(sum(map(len, s[i:i + 99])) + 100, minim)
print(minim)
