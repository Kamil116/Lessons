f = open('26_6__3ck46__3eqey.txt')
n = int(f.readline())
k = int(f.readline())
rooms = [[-1 for _ in range(k)] for _ in range(3)]
clients = [list(map(int, line.split())) for line in f.readlines()]
clients.sort(key=lambda x: (x[0], -x[2]))

occupied = 0
revenue = 0
for client in clients:
    start, end, money = client
    ok = False
    if money >= 300:
        for i in range(len(rooms[2])):
            if start > rooms[2][i]:
                rooms[2][i] = end
                ok = True
                occupied += 1
                revenue += 300
                break
    if money >= 200 and not ok:
        for i in range(len(rooms[1])):
            if start > rooms[1][i]:
                rooms[1][i] = end
                ok = True
                occupied += 1
                revenue += 200
                break
    if money >= 100 and not ok:
        for i in range(len(rooms[0])):
            if start > rooms[0][i]:
                rooms[0][i] = end
                ok = True
                occupied += 1
                revenue += 100
                break
print(occupied, revenue)
