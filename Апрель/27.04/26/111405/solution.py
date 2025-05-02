f = open('5-26__6750i.txt')
k = int(f.readline())
n = int(f.readline())
clients = [list(map(int, line.split())) for line in f.readlines()]
clients.sort(key=lambda x: (x[0], -x[1]))

super_times = []
times = []
machines = [-1 for _ in range(k)]
for client in clients:
    start, end = client[0], client[1]
    for j in range(len(machines)):
        if start > machines[j]:
            if (j + 1) % 7 == 0:
                machines[j] = start + (end - start) // 1.5
                super_times.append((end - start) // 1.5)
            else:
                machines[j] = end
                times.append(end - start)
            break

maxim = -1000
for super_time in super_times:
    for time in times:
        if (super_time + time) % 19 == 0:
            maxim = max(maxim, super_time + time)
print(maxim)
