# 2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from ast import Mult
import random


def create_list(length_of_array: int, min_for_random: int, max_for_random: int) -> list:
    list_of_numbers = []
    for i in range(0, length_of_array):
        list_of_numbers.append(random.randint(min_for_random, max_for_random))
    return list_of_numbers


def multi_pairs(list_of_numbers):
    new_list = []
    for i in range(0, int(len(list_of_numbers)/2)):
        new_list.append(
            list_of_numbers[i] * list_of_numbers[-(i+1)])
    if len(list_of_numbers) % 2 != 0:
        new_list.append(
            list_of_numbers[len(list_of_numbers) % 2+1] ** 2)
    return new_list

list_of_numbers = create_list(10, 1, 10)
print(list_of_numbers)
print(multi_pairs(list_of_numbers))
