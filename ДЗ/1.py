# print('Введите день недели:')
# day = int(input())

# if day == 6 or day == 7:
#    print('да')
#else:
#    print('нет')

# Задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#print('Левая часть выражения ¬(X ⋁ Y ⋁ Z)  Правая часть выражения ¬X ⋀ ¬Y ⋀ ¬Z \n')
#print('  x  \t  y  \t  z \tРезультат      x \t y  \t  z  \tРезультат\n')
#for x in [True,False]:
#     for y in [True,False]:
#         for z in [True,False]:
#             print(f'{x}\t{y}\t{z}\t {not(x or y or z)} \t |   {x}\t{y}\t{z}\t{not x and not y and not z}')
            
#print('\nРезультет левой и правой чатсей выражения идентичен, тождественность доказана\n') 
   
#Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3          

# x = int(input('Введите X: '))
# y = int(input('Введите Y: '))

# if x > 0 and y > 0:
#     print (f'X = {x}; Y = {y} -> 1')
# elif x<0 and y>0:
#     print (f'X = {x}; Y = {y} -> 2')
# elif x<0 and y<0:
#     print(f'X = {x}; Y = {y} -> 3')
# elif x>0 and y<0:
#     print(f'X = {x}; Y = {y} -> 4')
# else:
#     print('Точка лежит на оси координат')

#Задача 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# quater = int(input('Введите номер четверти от 1 до 4: '))

# if quater == 1:
#     print ('X > 0; Y > 0')
# elif quater == 2:
#     print ('X < 0; Y > 0')
# elif quater == 3:
#     print ('X < 0; Y < 0')
# elif quater == 4:
#     print ('X > 0; Y < 0')
# else:
#     print('Введенное значение четверти вне возможного диапазона')

#Задача 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

#from math import sqrt

#print('Введите координаты первой точки:')
#x1 = float(input('x1: '))
#y1 = float(input('y1: '))

#print('Введите координаты второй точки:')
#x2 = float(input('x2: '))
#y2 = float(input('y2: '))

#length = round(sqrt((x2-x1)**2+(y2-y1)**2),2)

#print(length)