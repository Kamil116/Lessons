f = open('26_1__6k161.txt')
n = int(f.readline())
orders = [list(map(int, line.split())) for line in f.readlines()]
orders.sort(key=lambda x: x[1])

prices = [order[2] for order in orders]
times = [order[1] - order[0] + 1 for order in orders]
for i in range(n):
    for j in range(i):
        if orders[i][0] > orders[j][1]:
            if orders[i][2] + prices[j] > prices[i]:
                prices[i] = orders[i][2] + prices[j]
                times[i] = times[j] + (orders[i][1] - orders[i][0] + 1)

print(max(prices))
for i in range(n):
    if prices[i] == max(prices):
        print(times[i])  # Длительность всех выбранных съемок
