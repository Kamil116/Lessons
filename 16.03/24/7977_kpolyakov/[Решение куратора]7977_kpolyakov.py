from re import *


def my_eval(string):
    number = ''
    my_string = ''
    for i in range(len(string)):
        if string[i] in '012345':
            number += string[i]
        else:
            my_string += str(int(number, 6))
            my_string += string[i]
            number = ''
    if number != '':
        my_string += str(int(number, 6))
    return my_string


f = open('24-314.txt')
s = f.readline()

num = '(?:[1-5][0-5]*|0)'
pattern = f'{num}(?:[*+]{num})*'
res = findall(pattern, s)
print(eval(my_eval(max(res, key=len))))
