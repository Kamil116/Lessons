from re import findall

f = open('../files/Задание_24__gmt4__rjfi.txt')
s = f.readline()

# pattern = '[BCDF]*' # первый вариант
pattern = '[^AE]*'
res = findall(pattern, s)
print(len(max(res, key=len)))
