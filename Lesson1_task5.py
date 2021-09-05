"""
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

letter1 = ord(input("Введите первую букву "))
letter2 = ord(input("Введите вторую букву "))
print(chr(letter1), (letter1 - ord('a')) + 1)
print(chr(letter2), (letter2 - ord('a')) + 1)
print(f"Между буквами {chr(letter1)} и {chr(letter2)}", letter2 - letter1 - 1, "букв/ы")