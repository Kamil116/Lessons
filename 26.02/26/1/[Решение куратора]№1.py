from math import ceil

f = open('26-61.txt')
n, m = map(int, f.readline().split())
videos = []
images = []
for i in range(n):
    new_file = int(f.readline())
    if new_file >= 101:
        videos.append(new_file)
    else:
        images.append(new_file)
videos.sort()
images.sort()
half = ceil(m / 2)

total_sum = 0
cnt = 0
last_vid = 0
for i in range(len(videos)):
    total_sum += videos[i]
    cnt += 1
    if total_sum >= half:
        last_vid = i
        break
all_files = sorted(videos[last_vid + 1:] + images)
ost = total_sum - half
# print(any([ost == elem for elem in videos]))

last_image = 0
total_sum -= ost
cnt -= 1
for j in range(len(all_files)):
    if all_files[j] + total_sum <= m:
        total_sum += all_files[j]
        cnt += 1
        last_image = j

print(cnt, total_sum)
