# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/sH87m)

fib_range = int(input("Введите число: "))


def fibonachi_plus(fib_range: int) -> list:
    flibonachi_list = [0, 1]
    if fib_range > 1:
        for i in range(2, fib_range+1):
            flibonachi_list.append(flibonachi_list[i-1]+flibonachi_list[i-2])
    return flibonachi_list


def fibonachi_minus(fib_range: int) -> list:
    flibonachi_list = [0, 1]
    if fib_range > 1:
        for i in range(2, fib_range+1):
            flibonachi_list.append(flibonachi_list[i-2]-flibonachi_list[i-1])
    return flibonachi_list


def sort_array(list_of_numbers: list):
    for i in range(0, int(len(list_of_numbers)/2)):
        list_of_numbers[i], list_of_numbers[-(1+i)
                                            ] = list_of_numbers[-(1+i)], list_of_numbers[i]


def fibonachi(fib_range: int) -> list:
    fib_plus = fibonachi_plus(fib_range)
    flibonachi_list = fibonachi_minus(fib_range)
    sort_array(flibonachi_list)
    for i in range(1, fib_range+1):
        flibonachi_list.append(fib_plus[i])
    return flibonachi_list


fib_list = fibonachi(fib_range)
print(f"for k = {fib_range} -> {fib_list}")
