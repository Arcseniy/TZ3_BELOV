# Небольшое предисловие
# Все файлы, которые мы хотим протестировать записываем в список file_names вручную (их полный путь)
# Переходим в конфигурацию pytest_TZ3 и запускаем

import timeit

file_names = ['/Users/arseniybelov/PycharmProjects/TZ3/TZ3_TEST_1.txt',
              '/Users/arseniybelov/PycharmProjects/TZ3/TZ3_TEST_2.txt',
              '/Users/arseniybelov/PycharmProjects/TZ3/TZ3_TEST_3.txt']

# Функция, которая считывает файл и записывает числа в список


def file_read(file_name):
    arr = []
    with open(file_name, 'r') as file:
        for line in file:
            for i in line.split():
                if i.isdigit():
                    arr.append(i)
                elif i[0] == "-":
                    arr.append(i)
    arr = [float(i) for i in arr]
    return arr


# Функция, которая находит минимальное число в файле


def find_min_num(arr):
    start = arr[0]
    for i in range(len(arr)):
        if arr[i] < start:
            start = arr[i]
    return start


# Функция, которая находит максимальное число в файле


def find_max_num(arr):
    start = arr[0]
    for i in range(len(arr)):
        if arr[i] > start:
            start = arr[i]
    return start


# Функция, которая находит сумму чисел в файле


def arr_sum(arr):
    ans = 0
# Обработка исключения, при слишком больших числах
    try:
        for i in arr:
            ans += i
        return ans
    except OverflowError:
        return 'inf'


# Функция, которая находит произведение чисел в файле


def arr_multiply(arr):
    if arr:
        ans = 1
    else:
        return 0
# Обработка исключения, при слишком больших числах
    try:
        for i in arr:
            ans *= i
        return ans
    except OverflowError:
        return 'inf'


# Вспомогательная функция для функции подсчёта времени скрипта (она компонует все предыдущие функции в одну)


def func_for_func():
    for file_name in file_names:
        arr = file_read(file_name)
        find_min_num(arr)
        find_max_num(arr)
        arr_sum(arr)
        arr_multiply(arr)


# Словарь для записи файла в ключ и времени работы скрипта с этим файлом в значение

res = {}

# Функция, которая считает время работы скрипта и записывает результаты в специальный файл


def script_time(file_name):
    res_time = timeit.timeit("func_for_func()", globals=globals(), number=50)
    res[file_name] = res_time
    s = file_name + " -- " + str(res[file_name])
    with open('/Users/arseniybelov/PycharmProjects/TZ3/RESULTS.txt', "a") as file:
        file.write(s + "\n")
    return res_time


# Функция, которая находит все чётные числа в файле - 4 пункт


def find_all_even(arr):
    cur = []
    for i in arr:
        if i % 2 == 0:
            cur.append(i)
    return cur
