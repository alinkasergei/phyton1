# 1/ Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [2, 3, 5, 9, 3]
print(sum(lst[1::2]))

# 2/ Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list = [2, 3, 5, 6]
def mult_elements(list):
    new_list = []
    for i in  range (len(list) - len(list) // 2):
        new_list.append(list[i] * list[-(i + 1)])
    print(new_list)
    return new_list
mult_elements(list)

# 3/ Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

#Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def func_minVSmax(arr):
    print(arr)
    res = [arr[0] % 1,arr[0] % 1,0] # res[min,max,buffer]
    for i in range(len(arr)):
        res[2] = round(arr[i] % 1, 2)
        if res[2] < res[0] and res[2] != 0:
            res[0] = res[2]
        elif res[2] > res[1]:
            res[1] = res[2]
    return round(res[1]-res[0],2)

test = [1.1, 1.2, 3.1, 5, 10.01]
print('min - max(test):',func_minVSmax(test))

# 5/Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример: 45 -> 101101  // 3 -> 11 // 2 -> 10

def funk_in01(n):
    num = ''
    while n > 0:
        num = str(n % 2) + num
        n//=2
    return num

n = int(input())
print(funk_in01(n))

# 6/ Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример: для k = 8 писок будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def funk_febonachi(n):
    ans_arr = [0]
    j = 1
    for i in range(1,n+1):
        if i%2 == 0:
            ans_arr.insert(0,-j)
        else:
            ans_arr.insert(0,j)
        ans_arr.append(j)
        j += ans_arr[-2]
    return ans_arr

n = int(input())
print(funk_febonachi(n))
