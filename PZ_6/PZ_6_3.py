# №3 Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
# списка влево на K позиций (при этом AN перейдет в AN-K, AN-1 — в AN-K-1, ..AK+1 — в
# A1, а исходное значение K первых элементов будет потеряно). Последние K элементов
# полученного списка положить равными 0.
import random  # импортирую модуль, чтобы в дальнейшем им пользоваться
k = int(input('Введите целое число: '))
n = int(input('Введите длину списка: '))

if k > 0 and n > k:  # обработка условия по заднию
    mylist = [random.randint(1, 100) for i in range(n)]  # создаю список с рандомными значениями и далее вывожу его
    mylist_copy = [el for el in mylist]  # копирую список, чтобы изменения в нем не влияли на изначальный список
    print('Наш список', mylist)
    for i in range(len(mylist)):  # решение задачи
        mylist_copy[i - k] = mylist[i]
    for i in range(len(mylist_copy) - k, len(mylist_copy)):
        mylist_copy[i] = 0
    print('Ответ: ', mylist_copy)  # ответ
else:
    print('Вы ввели неверные значения, не соответствующие условию задачи')