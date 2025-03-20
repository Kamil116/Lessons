# Ответ: 7348
f = open("26-61.txt")
n, m = map(int, f.readline().split())
files = [int(line) for line in f.readlines()]

videos = list(filter(lambda x: x > 101, files))
images = list(filter(lambda x: x <= 100, files))
videos.sort()

half = m // 2
taken_videos = []
i = 0
while sum(taken_videos) < half:
    taken_videos.append(videos[i])
    i += 1
zapas = sum(taken_videos) - half
taken_videos.remove(zapas)  # !!!!

remain = m - sum(taken_videos)
images.sort()
taken_images = []
i = 0
while sum(taken_images) + sum(taken_videos) < m:
    taken_images.append(images[i])
    i += 1
taken_images.pop(-1)

print(len(taken_images) + len(taken_videos))
