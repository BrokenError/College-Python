#  Дана строка. Подсчитать количество содержащихся в ней цифр
s = input('Введите строку: ')  # ввод данных
n = 0
for i in s:  # решение задачи
    if i.isdigit():
        n += 1
print(f'В строке {s}')  # ответ 7-8 строка
print(f'Ответ: {n} цифр')