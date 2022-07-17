# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def create_list(length_of_array: int, min_for_random: int, max_for_random: int) -> list:
    list_of_numbers = []
    for i in range(0, length_of_array):
        list_of_numbers.append(random.randint(min_for_random, max_for_random))
    return list_of_numbers
 
def list_of_odd(list_of_numbers):
    list_of_odd = []
    for i in range(len(list_of_numbers)):
        if i % 2 > 0:
            list_of_odd.append(list_of_numbers[i])
    return list_of_odd
 
list_of_numbers = create_list(10, 1, 10)
odd_nums = list_of_odd(list_of_numbers)
print('Заданный массив', list_of_numbers)
print('Нечетные элементы', odd_nums)
print('Сумма элементов на нечетных позициях =', sum(odd_nums))