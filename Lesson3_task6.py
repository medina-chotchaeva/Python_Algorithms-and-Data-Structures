"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

array = [randint(0, 100) for i in range(10)]
print(array)
max_index = array.index(max(array))
min_index = array.index(min(array))
if min_index < max_index:
    print(sum(array[min_index+1: max_index]))
else:
    print(sum(array[max_index+1: min_index]))