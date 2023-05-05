"""Сгенерируйте массив из целых чисел, содержащий 100 000 элементов, с помощью функции randomint из модуля random.

Сгенерируйте с помощью функции range массив, содержащий словари со следующей структурой:

{
	“num_1”: randomint(1,1_000_000),
	“num_2”: randomint(1,1_000_000)
}

Длина массива должна составлять 100 000 элементов.

Напишите функцию алгоритма сортировки пузырьком и с её помощью отсортируйте первый массив.

Отсортируйте второй массив с помощью встроенного спиского метода .sort() и лямбда-функции сначала по первому ключу, потом по второму
"""
import random

array = [random.randint(-50, 50) for i in range(100000)]
print(array)

new_array = []
for i in range(100000):
    new_array.append(
        {
            "num_1": random.randint(1, 1000000),
            "num_2": random.randint(1, 1000000)
        }
    )
print(*new_array, sep="\n")

def bubble_sort(n_array):
    n = len(n_array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if n_array[j] > n_array[j + 1]:
                bubble = n_array[j]
                n_array[j] = n_array[j + 1]
                n_array[j + 1] = bubble
    return n_array

n_array = [random.randint(-50, 50) for i in range(100000)]
sorted_n_array = bubble_sort(n_array)
print(sorted_n_array)


new_array = []
for i in range(100000):
    new_array.append(
        {
            "num_1": random.randint(1, 1000000),
            "num_2": random.randint(1, 1000000)
        }
    )

new_array.sort(key=lambda x: x["num_1"])
print(new_array)

new_array.sort(key=lambda x: x["num_2"])
print(new_array)


