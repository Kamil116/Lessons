f = open('26.txt')
n = int(f.readline())
clicks = [int(x) for x in f]
clicks.sort()

cur_clicks = 0
cur_limit = clicks[0] + 1000
ignored = []
registered = 0
for i in range(n):
    if clicks[i] < cur_limit:
        if cur_clicks == 5:
            ignored.append(i)
        else:
            registered += 1
            cur_clicks += 1
    else:
        cur_limit = clicks[i] + 1000
        cur_clicks = 1
        registered += 1

cur = 0
maxim = -1
for i in range(len(ignored) - 1):
    if ignored[i + 1] - ignored[i] == 1:
        cur += 1
        maxim = max(maxim, cur + 1)
    else:
        cur = 0
print(registered, maxim)
