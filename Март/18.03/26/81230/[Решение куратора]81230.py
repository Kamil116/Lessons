f = open('26_6__3ck48__3t75n.txt')
n = int(f.readline())
k = int(f.readline())
rooms = [[-1 for _ in range(k)] for _ in range(3)]
# создаём 3 этажа по k (20) комнат в каждом
clients = [list(map(int, line.split())) for line in f.readlines()]
# считываем всех клиентов
clients.sort(key=lambda x: (x[0], -x[1]))
# сортируем клиентов, сначала возрастанию времени прихода, потом
# по убыванию ухода, то есть если пришли одновременно, важнее тот, кто уйдёт позже

clients_money = 0  # оставшееся количество денег у заселившихся
revenue = 0  # выручка, количество денег, которое БУ заработает
for client in clients:
    # проходимся по клиентам, достаём время прихода, ухода, деньги
    start, end, money = client
    if money >= 300:
        for i in range(len(rooms[2])):
            if start > rooms[2][i]:
                # если время прихода больше последней минуты, когда номер занят
                # "Следующий гость может занять комнату в следующую минуту после освобождения"
                rooms[2][i] = end
                revenue += 300
                clients_money += money - 300
                break
    elif money >= 200:
        for i in range(len(rooms[1])):
            if start > rooms[1][i]:
                rooms[1][i] = end
                revenue += 200
                clients_money += money - 200
                break
    elif money >= 100:
        for i in range(len(rooms[0])):
            if start > rooms[0][i]:
                rooms[0][i] = end
                revenue += 100
                clients_money += money - 100
                break

print(clients_money, revenue)
