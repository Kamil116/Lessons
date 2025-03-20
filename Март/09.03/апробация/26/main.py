f = open('26.txt')
n, k = map(int, f.readline().split())
s = [list(map(int, i.split())) for i in f]
a = []
for i in s:
    a.append([i[0], sum(i[1:]), i[-1]])
a = sorted(a, key=lambda x: (-x[1], -x[2], x[0]))
for i in a:
    if i[1] >= 280:
        print(i)

print(a[k - 1])
count = 0
for i in a:
    if i[1] == 279:
        print(i)
        count += 1
print(count)
