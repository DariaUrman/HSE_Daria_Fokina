"""1. Создайте ряд функций для проведения математических вычислений:

Функция вычисления факториала числа (произведение натуральных чисел от 1 до n).
Принимает в качестве аргумента число, возвращает его факториал.

Поиск наибольшего числа из трёх.
Принимает в качестве аргумента кортеж из трёх чисел, возвращает наибольшее из них.

Расчёт площади прямоугольного треугольника.
Принимает в качестве аргумента размер двух катетов треугольника. Возвращает площадь треугольника.
"""
# Функция вычисления факториала числа

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

# Поиск наибольшего числа из трех
def maximum (a,b,c):
   list=[a,b,c]
   return max(list)

a = int(input("Введите число"))
b = int(input("Введите число"))
c = int(input("Введите число"))
print(maximum (a,b,c))

# Расчёт площади прямоугольного треугольника

a=int(input("Длина первого катета"))
b= int(input("Длина второго катета"))

print (a * b/2)

""""Создайте функцию для генерации текста с адресом суда.

Функция должна по шаблону генерировать шапку для процессуальных документов с реквизитами сторон для отправки.

Пример работы функции:

В арбитражный суд города Москвы
Адрес: 115225, г. Москва, ул. Б. Тульская, 17

Истец: Пупкин Василий Геннадьевич
ИНН 1236182357 ОГРНИП 218431927812733
Адрес: 123534, г. Москва, ул. Опущенных водников, 13

Ответчик: ООО “Кооператив Озеро”
ИНН 1231231231 ОГРН 123124129312941
Адрес: 123534, г. Москва, ул. Красивых молдавских партизан, 69

Номер дела А40-123456/2023

Функция должна принимать в качестве аргумента словарь с данными ответчика и номером дела (ссылка на файл с данными). 

На основании номера дела из списка судов должен быть выбран корректный суд для отправки (данные по арбитражным судам также имеются в указанном выше файле). Используйте код суда из дела
С помощью f-string создайте шаблон для заполнения
В качестве истца укажите свои данные (данные студента)
В данные по ответчику подставьте данные, переданные в функцию в качестве аргумента
В конце шапки подставьте номер дела

Функция должна возвращать готовую шапку в виде строки.

Создайте ещё одну функцию, которая принимает в себя список словарей с данными ответчика. Используйте цикл for для генерации всех возможных вариантов данной шапки с вызовом первой функции внутри тела цикла for и выводом данных. которые она возвращает в консоль.
"""

