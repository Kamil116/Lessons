# Решение Тани
f = open('776')
n = (int(f.readline()))
a = [int(i) for i in f]
a.sort()
d = []
d.append(a[0])
for i in range(1, len(a) - 1):
    if a[i] / d[-1] >= 1.1:
        d.append(a[i])
print(len(d), d[-1])
