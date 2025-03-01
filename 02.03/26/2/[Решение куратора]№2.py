f = open('26-60.txt')
k, n = map(int, f.readline().split())
free_places = [int(f.readline()) for i in range(k)]
students = [list(map(int, line.split())) for line in f.readlines()]

abiturients = [[] for _ in range(k + 1)]
for i in range(n):
    student = students[i]
    spec_code = student[1]
    abiturients[spec_code].append(student[0])

enrolled = 0
max_comp = 0
min_points = -1
for i in range(k):
    abiturients_list = abiturients[i]
    abiturients_list.sort(reverse=True)
    enrolled += min(len(abiturients_list), free_places[i])
    if len(abiturients_list) / free_places[i] > max_comp:
        max_comp = len(abiturients_list) / free_places[i]
        min_points = abiturients_list[min(free_places[i] - 1, len(abiturients_list) - 1)]
print(enrolled, min_points)
# Ответ: 55255 266
