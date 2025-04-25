f = open("26_2M__3whpt.txt")
N, K = map(int, f.readline().split())
a = []
num = 1
for i in f:
    shlif, okras = map(int, i.split())

    a.append([shlif, "shlif", num])
    a.append([okras, "okras", num])

    num += 1
a.sort(key=lambda x: x[0])

added_tools = []
lenta = [0] * N

start = 0
end = N - 1

cnt_shlif = 0

for i in range(len(a)):
    if a[i][2] not in added_tools:
        if a[i][1] == "shlif":
            lenta[start] = a[i]
            cnt_shlif += 1
            start += 1
        else:
            lenta[end] = a[i]
            end -= 1
        added_tools.append(a[i][2])

print(cnt_shlif)
print(lenta[K - 1])  # 489 924
