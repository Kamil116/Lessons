f = open('26.txt')
n = int(f.readline())
teeth = [int(x) for x in f.readlines()]
teeth.sort()
taken = [teeth[0]]
for i in range(1, len(teeth)):
    if teeth[i] / taken[-1] >= 1.1:
        taken.append(teeth[i])
print(len(taken), taken[-1])
# 71 91862
