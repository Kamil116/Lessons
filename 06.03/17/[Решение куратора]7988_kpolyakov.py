def sum_digits(t):
    return sum(map(int, str(t)))


f = open('17-428.txt')
numbers = [int(x) for x in f.readlines()]
kr_531, kr_773 = 0, 0
for number in numbers:
    if number % 531 == 0:
        kr_531 += 1
    if number % 773 == 0:
        kr_773 += 1

cnt = 0
total_sum = 0
for i in range(len(numbers) - 2):
    x, y, z = numbers[i:i + 3]
    first = int(100 <= x <= 999) + int(100 <= y <= 999) + int(100 <= z <= 999)
    second = int(sum_digits(x) == kr_531) + int(sum_digits(y) == kr_531) + int(sum_digits(z) == kr_531)
    third = int(sum_digits(x) == kr_773) + int(sum_digits(y) == kr_773) + int(sum_digits(z) == kr_773)
    if first >= 1 and second <= 1 and third >= 2:
        cnt += 1
        total_sum += x + y + z
print(cnt, total_sum // cnt)
