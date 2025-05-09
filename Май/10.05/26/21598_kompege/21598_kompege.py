f = open('26_21598.txt')
n = int(f.readline())
clients = [0 for _ in range(1441)]
for _ in range(n):
    start, end = map(int, f.readline().split())
    for i in range(start, end):
        clients[i] += 1

cnt = 1
changed = []
for i in range(1, len(clients) - 1):
    if clients[i] != clients[i + 1]:
        changed.append(i + 1)

maxim = 0
for j in range(len(changed) - 1):
    maxim = max(maxim, changed[j + 1] - changed[j])
    
print(changed[-2], maxim)
