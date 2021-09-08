"""
Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
"""
def sum_left(n):
    if n == 1:
        return n
    summ = n + sum_left(n - 1)
    return summ


n = int(input('Введите натуральное число до 998 включительно: '))

left = sum_left(n)
right = n * (n + 1) // 2

print(f'left = {left}\n'
      f'right = {right}\n'
'Верно' if left == right
        else 'Неверно')
