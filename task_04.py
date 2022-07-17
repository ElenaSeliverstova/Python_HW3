# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите число: "))

def transfer_number(number: int) -> list:
    rest = number
    list_of_numbers = []
    while rest >= 1:
        rest = number // 2
        list_of_numbers.append(number-rest*2)
        number = rest
    sort_array(list_of_numbers)
    return convert_list_in_int(list_of_numbers)

def sort_array(list_of_numbers: list):
    for i in range(0, int(len(list_of_numbers)/2)):
        list_of_numbers[i], list_of_numbers[-(1+i)
                                              ] = list_of_numbers[-(1+i)], list_of_numbers[i]

def convert_list_in_int(list_of_numbers: list) -> int:
    result = ""
    for i in list_of_numbers:
        result = result + str(i)
    return int(result)

result = transfer_number(number)
print(f" - {number} -> {result}") 