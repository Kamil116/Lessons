def binsearch(arr, val):
    left = 0
    right = len(arr) - 1
    while right - left > 1:
        middle = (left + right) // 2
        if val >= arr[middle]:
            left = middle
        elif val <= arr[middle]:
            right = middle
    return arr[left]


f = open('26_18541.txt')
n, m = map(int, f.readline().split())

weights = []
for i in range(n):
    weights.append(int(f.readline()))

athletes = []
for i in range(m):
    athletes.append(int(f.readline()))

weights.sort()
chosen_weights = {}
for i in range(m):
    can_take = athletes[i]
    cur_weight = binsearch(weights, can_take)
    chosen_weights[cur_weight] = chosen_weights.get(cur_weight, 0) + 1

sum_weights = 0
cnt_weights = 0
max_frequency = 0
max_frequency_weight = None
for weight in chosen_weights:
    cnt_weight = chosen_weights[weight]
    sum_weights += weight * cnt_weight
    cnt_weights += cnt_weight
    if cnt_weight > max_frequency:
        max_frequency = cnt_weight
        max_frequency_weight = weight
print(int(sum_weights / cnt_weights), max_frequency_weight)
