f = open('26.txt')
n, k = map(int, f.readline().split())
candidates = []
for line in f.readlines():
    candidate_id, first, second, third, interview = map(int, line.split())
    sum_points = first + second + third + interview
    candidates.append([sum_points, interview, candidate_id])
candidates.sort(key=lambda x: (-x[0], -x[1], x[2]))

added_points = []
for i in range(len(candidates)):
    cur_point = candidates[i][0]
    if cur_point in added_points:
        continue

    cur_point_candidates = 0
    added_points.append(cur_point)
    for j in range(len(candidates)):
        if candidates[j][0] == cur_point:
            cur_point_candidates += 1
    if cur_point_candidates > k:
        print(candidates[i - 1][2], cur_point_candidates)
        break
    k -= cur_point_candidates
