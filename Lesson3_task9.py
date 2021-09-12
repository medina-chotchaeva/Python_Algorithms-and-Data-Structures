"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import random

mat_1 = []
for i in range(4):
    mat_2 = []
    for n in range(4):
      num = int(random()*20)
      mat_2.append(num)
      print('%4d' % num, end='')
    mat_1.append(mat_2)
    print()

mx = -1
for n in range(4):
    mn = 100
    for i in range(4):
        if mat_1[i][n] < mn:
            mn = mat_1[i][n]
    if mn > mx:
        mx = mn
print("Максимальный элемент среди минимальных элементов столбцов матрицы: ", mx)