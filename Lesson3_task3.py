"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

array = [randint(0, 100) for i in range(10)]
print(array)
mx = array.index(max(array))
mn = array.index(min(array))
array[mx], array[mn] = array[mn], array[mx]
print(array)