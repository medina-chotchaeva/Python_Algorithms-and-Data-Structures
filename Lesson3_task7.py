"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
from random import random

array = [round(random() * 100) for _ in range(100)]
print(f'Массив: {array}')

min_index_1 = 0
min_index_2 = 1

for i in array:
    if array[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = array.index(i)
    elif array[min_index_2] > i:
        min_index_2 = array.index(i)

print(f'Два наименьших элемента: {array[min_index_1]} и {array[min_index_2]}')