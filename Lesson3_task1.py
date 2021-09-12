"""
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

array = {}
for div in range(2, 9):
    array[div] = []
    for divisible in range(2, 99):
        if divisible % div == 0:
            array[div].append(divisible)
    print(f'Числу {div} кратны {len(array[div])} чисел: {array[div]}.')