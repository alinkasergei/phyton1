"""1) Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

Пример:

Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}"""
from tokenize import maybe


n=int(input('Введите число: '))
my_dict=[]
for i in range(1,n+1):
    my_dict.append([i,3*i+1])
print(dict(my_dict))

""" #2 Напишите программу, которая принимает на вход число N 
и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

#from math import factorial

#n = int(input("enter number: "))
#list = []
#for i in range(1, n + 1):
#    list.append(factorial(i))
#print(list)
"""3) Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.

Пример:

Для n = 5: сумма = 11,55 """

#n = int(input('Введите число: '))
#my_list = [round(((1+1/n)**n),2) for n in range(1,n+1)]
#print('Последовательность чисел: ', my_list)
#print('Сумма чисел последовательности: ', sum(my_list))

# #4 Задайте число N и создайте список, заполненный числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt: в одной строке одно число.

# n = int(input("Введите число: "))
# while n <= 0:
# n = int(input("Укажите целое число больше нуля: "))

# fileW = open("text.txt", "w")
# for i in range(-n, n + 1):
# if i != 0:
# fileW.write(str(i) + "\n")
# fileW.close()

# mult = 1
# fileR = open("text.txt", "r")
# for line in fileR:
#
# mult *= int(line)
# fileR.close()

# print(f'Произведение: {mult}')

# 5) Реализуйте алгоритм перемешивания списка.
# (Без использования библиотеки random)

# import datetime # подключение библиотеки
# import time

# spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random_spisok = [None] * len(spisok)
# j = 1
#
# def random (spisok):
#    for i in range(len(spisok)):
#       index = datetime.datetime.now().microsecond % 10 # получаем милисекунды и получаем остаток от деления на 10 (рандомное число от 0 до 9 )
#       random_spisok[i] = spisok[index]
#       time.sleep(0.3)
#   print(random_spisok)

# random (spisok)