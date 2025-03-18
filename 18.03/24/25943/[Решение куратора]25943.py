from re import findall

f = open('../files/Задание_24__f6wk__swpe.txt')
s = f.readline()

# 11199988766... не 3, 5
pattern = '[01246789]*'
# pattern = '[^35]*' # второй вариант
res = findall(pattern, s)
print(len(max(res, key=len)))
