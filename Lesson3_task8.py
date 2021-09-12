"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = []

for i in range(4):
    matrix.append([])
    sum_ = 0
    for n in range(4):
        user_num = int(input(f'Введите {i+1} элемент {n+1} столбца: '))
        sum_ += user_num
        matrix[i].append(user_num)

    matrix[i].append(sum_)

for a in matrix:
    print(('{:>4d}' * 5).format(*a))
