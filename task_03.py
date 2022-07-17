# 3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5.567, 10.03] => 0.564 или 564

import random

def create_float_list(length_of_array: int) -> list:
    list_of_numbers = []
    for i in range(0, length_of_array):
        list_of_numbers.append(round(random.random()*10, 3)) 
        # 'random.random' - получаем значения float от 1 до 10, '* 10' - увеличиваем диапозон, ',3' - округляем до 3 знаков
    return list_of_numbers

def diff_of_float(list_of_numbers : list) -> int:
    max = list_of_numbers[0] - int(list_of_numbers[0])
    min = list_of_numbers[0] - int(list_of_numbers[0]) 
    for i in list_of_numbers:
        num = i - int(i)
        if num > max:
            max = num
        if num < min:
            min = num
    return min,max

list_of_numbers = create_float_list(5)
min,max = diff_of_float(list_of_numbers)
dif = max - min
print(f"{list_of_numbers} => max({max:.3f}) - min({min:.3f}) = {dif:.3f}") 