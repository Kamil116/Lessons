f = open('26_4_1709312020.txt')
l, p, n = map(int, f.readline().split())
lots = {}
for i in range(n):
    lot_number, participant_number, bet = map(int, f.readline().split())
    if lot_number in lots:
        lots[lot_number].append(bet)
    else:
        lots[lot_number] = [bet]

cnt = 0
total_sum = 0
for lot in lots:
    if len(lots[lot]) >= 2:
        cnt += 1
        total_sum += sorted(lots[lot])[-2]
print(cnt, total_sum)
