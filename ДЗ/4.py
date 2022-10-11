# 1. Вычислить число c заданной точностью d

# Пример: при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

from math import pi

d = int(input("Введите число для заданной точности числа Пи:\n"))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число N: '))
empty_list = []
for i in range(0, n - 1):
    if n % (n - i) == 0:
        empty_list.append((int(n / (n - i))))
print(f'Список простых множителей для числа N={n}: {empty_list}')

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint

some_list = []
i = 1
n = int(input('Введите количество элементов в списке: '))
for i in range(n):
    some_list.append(randint(1, 5))
    i += 1
print(f'Ваш случайно сгенерированный список из {n} элементов: {some_list}')
unique_list = list(set(some_list))
print(f'Список уникальных элементов {unique_list}')

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# -  k=4 => 2*x^4 + 4*x^3 + 5x^2  - 3x + 3 = 0

import random

k = (int(input("k = ")))
list1 = []
k = 3
for i in range(k, 0, -1):
    c = random.randint(0, 100)
    a = (f'{c}x^{i} + ')
    list1.append(a)

b = (f'{random.randint(0,100)} = 0\n')
list1.append(b)
listToStr = ' '.join([str(elem) for elem in list1])
print(listToStr)

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from random import choice

def poly_sum(name_1: str, name_2: str):
    with open(name_1, 'r', encoding='utf-8') as my_f_1, \
            open(name_2, 'r', encoding='utf-8') as my_f_2:
        first = my_f_1.readlines() # .readlines() возвращает список строк всех, которые находятся в файле.
        second = my_f_2.readlines()

        if len(first) == len(second): # Условие совпадения количества строк.
            with open('sum_poly.txt', 'a', encoding='utf-8') as my_f_3:
                for i, v in enumerate(first):           # enumerate - как range, но возвращает кортеж
                        # состоящий из индекса и значения! Поэтому мы кортеж распаковывем в пер-х i и v!
                    my_f_3.write(f'{v[:-5]} + {second[i]}') # отрезаем 5 от конца: = 0\n
        else:
            print('The contents of the files do not match!')


# poly_sum(input('Enter the file name "text_1.txt": '), input('Enter the file name "text_2.txt": '))
poly_sum('poly.txt', 'poly_2.txt')
