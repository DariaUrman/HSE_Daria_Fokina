"""Сгенерируйте с использованием функции range (случайный шаг от 3 до 5) массив, содержащий отсортированные числа от 10 до 250 млн.

Можно использовать функцию randomint из модуля random для ещё большей рандомизации значений, но для целей работы алгоритма бинарного поиска проследите, чтобы значения в массиве были отсортированы.

Сгенерируйте с помощью list comprehensions и функции randomint (встроенный модуль random) 10 случайных чисел.

Напишите функцию для алгоритма линейного поиска.

Напишите функцию для алгоритма бинарного поиска.

Проверьте наличие ранее сгенерированных случайных чисел в массиве с помощью алгоритмов линейного и бинарного поиска, замерьте время

"""
import random

start = 10
stop = 250000000
step = random.randint(3, 5)

r_array = list(range(start, stop, step))
print(r_array)

r_list = [random.randint(10, 250000000) for i in range(10)]
print(r_list)

import time
def linear_search(r_array, element):
    start_t = time.time()
    for i in range(len(r_array)):
        if r_array[i] == element:
            duration = time.time()-start_t
            return i, duration
    else:
        duration = time.time() - start
        return -1, duration
def binary_search(r_array, a):
    start_tb = time.time()
    first = 0
    last = len(r_array) - 1
    index = -1
    while first <= last and index == -1:
        mid_val = (first + last) // 2
        if r_array[mid_val] == a:
            index = mid_val
        else:
            if a < r_array[mid_val]:
                last = mid_val - 1
            else:
                first = mid + 1
        duration_tb = time.time() - start_tb
    return index, duration_tb

