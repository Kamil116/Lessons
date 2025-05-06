f = open('26-156.txt')
n = int(f.readline())
points = list(map(int, f.readline().split()))
scores = []

for i in range(n):
    line = list(map(int, f.readline().split()))
    student_id = line[0]
    students_scores = line[1:]
    sum_points = 0
    penalty = 0
    skipped = 0

    for j in range(len(students_scores)):
        if students_scores[j] == 1:
            sum_points += points[j]
        elif students_scores[j] == -1:
            penalty += points[j]
        elif students_scores[j] == 0:
            skipped += 1

    scores.append([student_id, sum_points - penalty, penalty, skipped])

scores.sort(key=lambda x: (-x[1], x[2], x[3], x[0]))
last_winner = scores[len(scores) // 4 - 1]
winners = scores[:len(scores) // 4]
for i in range(len(scores) // 4, len(scores)):
    if scores[i][1:] == last_winner[1:]:
        winners.append(scores[i])
    else:
        print(scores[i][0])
        break

target = scores[999]  # участник, занявший 1000 место
print(len(list(filter(lambda x: x[1] == target[1] and x[2] == target[2] and x[3] == target[3], scores))))
