f = open('17-426.txt')
numbers = [int(num) for num in f.readlines()]
max_abs_num = max(abs(min(numbers)), max(numbers))
max_num = max(numbers)
cnt, total_sum = 0, 0

for i in range(len(numbers) - 2):
    x, y, z = numbers[i:i + 3]
    first = int(1000 <= abs(x) <= 9999) + int(1000 <= abs(y) <= 9999) + int(1000 <= abs(z) <= 9999)
    second = int(abs(x) % 10 == max_abs_num % 10) + int(abs(y) % 10 == max_abs_num % 10) + int(
        abs(z) % 10 == max_abs_num % 10)
    third = int(abs(x) % 10 == max_num % 10) + int(abs(y) % 10 == max_num % 10) + int(abs(z) % 10 == max_num % 10)
    if first >= 1 and second <= 1 and third >= 1:
        cnt += 1
        total_sum += x + y + z
print(cnt, total_sum // cnt)
