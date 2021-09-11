"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""

from random import random

array = [round(random() * 100 - 101) for _ in range(100)]
print(f'Массив: {array}')

max_index = 0

for i in array:
    if array[max_index] < i:
        max_index = array.index(i)
print(f'Максимальный отрицательный элемент массива: {array[max_index]}, позиция: {max_index}')