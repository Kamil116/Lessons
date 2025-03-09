# Решение Риты
f = open('26.txt')
m, p = map(int, f.readline().split())
s = [list(map(int, i.split())) for i in f]
s = sorted(s, key=lambda x: (x[0], -x[1]))
printer = [-1 for i in range(m)]
count = 0
for i in range(len(s)):
    flaf = 0
    for j in range(m):
        if (printer[j] <= s[i][0]):
            printer[j] = s[i][0] + s[i][1] + 3
            flaf = 1
            print(s[i][0] + s[i][1])
            break
    if flaf == 0:
        l = printer.index(min(printer))
        printer[l] += (s[i][1] + 3)
        if (printer[l] - 3) <= 480:
            count += 1
print(count)
