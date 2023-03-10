# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# -> 6 12

# Решение:
# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)

# n = int(input('Введите количество элементов для первого множества: '))
# m = int(input('Введите количество элементов для второго множества: '))

# first_list = []
# second_list = []

# print('Задайте элементы для первого множества:')
# for _ in range(n):
#     first_list.append(int(input()))

# print('Задайте элементы для второго множества:')
# for _ in range(m):
#     second_list.append(int(input()))

# result_list = []

# for i in range(n):
#     for j in range(m):
#         if first_list[i] == second_list[j]:
#             result_list.append(first_list[i])

# result_list = quicksort(list(set(result_list)))

# print(f'Числа, которые встречаются в обоих множествах => {", ".join(str(i) for i in result_list)}')


# Задача 22:  
# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод - на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# Пример:
# 4 -> 1 2 3 4
# 9

# Решение:
# number_of_bushes = int(input('Введите количество кустов: '))

# bushes = []

# print('Введите число ягод для каждого куста: ')
# for _ in range(number_of_bushes):
#     bushes.append(int(input()))

# max = 0
# temp = 0

# for i in range(number_of_bushes):
#     if i != number_of_bushes - 2 and i != number_of_bushes - 1:
#         temp = bushes[i] + bushes[i + 1] + bushes[i + 2]
#     elif i == number_of_bushes - 2:
#         temp = bushes[i] + bushes[i + 1] + bushes[0]
#     elif i == number_of_bushes - 1:
#         temp = bushes[i] + bushes[0] + bushes[1]

#     if temp > max:
#         max = temp

# print(f'Максимальное число ягод, которое можно собрать за один заход => {max}')
