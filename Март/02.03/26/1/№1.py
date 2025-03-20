# Решение Полины
f = open('26-61 (1).txt')
s = int(f.readline().split()[1])
v = []
j = []
c = 0
for i in f:
    if int(i) >= 101:
        v.append(int(i))
    if int(i) <= 100:
        j.append(int(i))
s2 = s // 2
v = sorted(v)
sm = 0
for h in v:
    if sm < s2:
        sm += h
        c += 1
print(sm - s2)
sm = sm - 165
os = s - sm
j = sorted(j)
smm = 0
for k in j:
    if smm + k <= os:
        smm += k
        c += 1
print(c - 1)
