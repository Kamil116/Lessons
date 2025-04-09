f = open('26_20970.txt')
n, k = map(int, f.readline().split())
clients = [list(map(int, line.split())) for line in f.readlines()]
clients.sort()
m = [[] for _ in range(k)]  # 0...11
util = 0
for i in range(len(clients)):
    start, duration, m_num = clients[i]
    queue = 0
    if m_num != 0:
        for j in range(len(m[m_num - 1])):
            if m[m_num - 1][j] > start:
                queue += 1
        if queue <= 4:
            if len(m[m_num - 1]) == 0:
                real_start = start
            else:
                real_start = max(m[m_num - 1][-1], start)
            m[m_num - 1].append(real_start + duration)
        else:
            util += 1
    else:
        min_queue = 10000
        min_queue_ind = None
        for j in range(len(m)):
            queue = 0
            for k in range(len(m[j])):
                if m[j][k] > start:
                    queue += 1
            if queue < min_queue:
                min_queue = queue
                min_queue_ind = j
        if min_queue <= 4:
            if len(m[min_queue_ind]) == 0:
                real_start = start
            else:
                real_start = max(m[min_queue_ind][-1], start)
            m[min_queue_ind].append(real_start + duration)
        else:
            util += 1
print(max(list(map(len, m))))
print(util)
