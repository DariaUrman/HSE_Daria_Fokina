"""Напишите функцию для валидации ИНН (идентификационного номера налогоплательщика), которая принимает в качестве аргумента строку, содержащую ИНН или просто набор цифр, похожий на ИНН.

Функция возвращает True в случае, если ИНН прошёл проверку, и False, если проверка не пройдена.

Для удобства лучше разбить код на несколько взаимосвязанных функций.

ТЗ составлено с использованием материалов Kholenkov.ru.

ИНН организации состоит из 10 цифр:
1-4-я цифры:
для российской организации — код налогового органа, который присвоил ИНН;
для иностранной организации — индекс, определяемый Федеральной налоговой службой;
5-9-я цифры:
для российской организации — порядковый номер записи о лице в территориальном разделе Единого государственного реестра налогоплательщиков налогового органа, который присвоил ИНН;
для иностранной организации — код иностранной организации (КИО) согласно Справочнику «Коды иностранных организаций»;
10-я цифра — контрольное число.

ИНН физического лица (индивидуального предпринимателя) состоит из 12 цифр:
1-4-я цифры — код налогового органа, который присвоил ИНН;
5-10-я цифры — порядковый номер записи о лице в территориальном разделе Единого государственного реестра налогоплательщиков налогового органа, который присвоил ИНН;
11-12-я цифры — контрольное число.

Алгоритм проверки ИНН организации (10 знаков)

Вычисляется контрольная сумма со следующими весовыми коэффициентами: (2, 4, 10, 3, 5, 9, 4, 6, 8, 0), т. е. необходимо вычислить сумму произведений цифр ИНН (с 1-й по 9-ю) на следующие коэффициенты — [2, 4, 10, 3, 5, 9, 4, 6, 8]:

2 * inn[0] + 4 * inn[1] + .... +  8 * inn[9]

Вычисляется контрольное число как остаток от деления контрольной суммы на 11 (оператор деления по модулю %).
Если контрольное число больше 9, то контрольное число вычисляется как остаток от деления контрольного числа на 10

Контрольное число проверяется с десятым знаком ИНН. В случае их равенства ИНН считается правильным.

Алгоритм проверки ИНН физического лица и ИП (12 знаков)

Необходимо вычислить сумму произведений цифр ИНН (с 1-й по 10-ю) на следующие коэффициенты — [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]:

7 * inn[0] + 2 * inn[1] + .... +  8 * inn[9]

Вычисляется первое контрольное число как остаток от деления контрольной суммы на 11. Если контрольное число больше 9, то контрольное число вычисляется как остаток от деления контрольного числа на 10

Необходимо вычислить сумму произведений цифр ИНН (с 1-й по 11-ю) на следующие коэффициенты — [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]:

3 * inn[0] + 7 * inn[1] + .... +  8 * inn[10]

Вычисляется второе контрольное число как остаток от деления контрольной суммы на 11. Если контрольное число больше 9, то контрольное число вычисляется как остаток от деления контрольного числа на 10

Первое контрольное число проверяется с одиннадцатым знаком ИНН, а второе контрольное число проверяется с двенадцатым знаком ИНН. В случае их равенства ИНН считается правильным.

"""

def inn_check_sums (nums, type):
    inn_check_type = {
        'n_10': [2, 4, 10, 3, 5, 9, 4, 6, 8],
    }
    n = 0
    t = inn_check_type[type]
    for i in range (0, len(t)):
        n += nums[i]*t[i]
    return n % 11 % 10
def inn_check (inn):
    n = str(inn)
    nums = [int(x) for x in n]
    if len(n) == 10:
        n_1 = inn_check_sums(nums, 'n_10')
        return n_1 == nums [-1], True
    else:
        return False
def inn_check_sums_ip_p (nums_ip_p, type_ip_p):
    inn_check_type_ip_p = {
        'n_2_12':[7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        'n_1_12': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
    }
    n_ip_p = 0
    t_ip_p = inn_check_type_ip_p [type_ip_p]
    for f in range (0, len(t_ip_p)):
        n_ip_p += nums_ip_p[f] * t_ip_p[f]
    return n_ip_p % 11 % 10
def inn_ip_p_check (inn_ip_p):
    n_ip_p = str(inn_ip_p)
    nums_ip_p = [int(y) for y in n_ip_p]
    if len(n_ip_p) == 12:
        n_2 = inn_check_sums_ip_p(nums_ip_p, 'n_2_12')
        n_1 = inn_check_sums_ip_p(nums_ip_p, 'n_1_12')
        return n_2 == nums_ip_p[-2] and n_1 == nums_ip_p[-1], True
    else:
        return False