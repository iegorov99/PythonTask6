'''
Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''

# import sys

# try:
#     first_number = int(input('Введите первый элемент прогрессии: '))
#     dif = int(input('Введите разность: '))
#     count = int(input('Введите количество элементов: '))
# except ValueError:
#     print('Это не число/введено неверное значение')
#     sys.exit()

# result = []
# for item in range(count) :
#     num = first_number + item * dif
#     result.append(num)

# print(result)

'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''

import sys
import random

try :
    count = int(input('Введите количество элементов массива: '))
except ValueError :
    print('Это не число/введено неверное значение')
    sys.exit()

array = []

for item in range(count) :
    num = random.randint(-10, 10)
    array.append(num)
    print(num, end = ' ')

print()

try :
    minimum = int(input('Введите минимум: '))
    maximum = int(input('Введите максимум: '))
except ValueError :
    print('Это не число/введено неверное значение')
    sys.exit()

if minimum > maximum :
    print('Минимальное значение не может быть больше максимального!')
elif maximum < min(array) or minimum > max(array):
    print('Значений в заданном диапозоне нет!')

for i in range(len(array)) :
    if array[i] >= minimum and array[i] <= maximum :
        print(i, end = ' ')
