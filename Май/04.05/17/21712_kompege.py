maxim = -72341983240
count = 0
minim = 1000000807
a = []
f = open('17_21712.txt')
for i in f:
    a.append(int(i))
    if 1000 <= (int(i)) <= 9999 and (int(i)) % 10 == 6:
        if int(i) < minim:
            minim = int(i)
for i in range(len(a) - 2):
    if (((1000 <= (abs(a[i])) <= 9999 and (abs(a[i]) % 10 == 6)) + (1000 <= abs(a[i + 1]) <= 9999 and (
            abs(a[i + 1])) % 10 == 6) + (1000 <= (abs(a[i + 2])) <= 9999 and abs(a[i + 2]) % 10 == 6)) == 1
            and a[i] + a[i + 1] + a[i + 2] <= minim):
        count += 1
        maxim = max(((a[i]) + a[i + 1] + a[i + 2]), maxim)
print(count, maxim)
