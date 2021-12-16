from TZ3_BELOV import *

arr = file_read('/Users/arseniybelov/PycharmProjects/TZ3/TZ3_TEST_1.txt')

# Тест функции, ищущей минимальное число


def test_find_min_num():
    assert find_min_num([0, 1, 2, 3]) == 3
    assert find_min_num([-228.228, -1337, 3.14]) == -1337
    assert find_min_num([-1.12, -1.05]) == -1.12


# Тест функции, ищущей максимальное число


def test_find_max_num():
    assert find_max_num([0, 1, 2, 3]) == 3
    assert find_max_num([-228.228, -1337, 3.14]) == 3.14
    assert find_max_num([-1.12, -1.05]) == -1.05


# Тест функции, считающей сумму чисел


def test_arr_sum():
    assert arr_sum([0, 1, 2, 3]) == 6
    assert arr_sum([-228.228, -1337, 3.14]) == -1562.088
    assert arr_sum([-1.12, -1.05]) == -2.17


# Тест функции, считающей произведение чисел


def test_arr_multiply():
    assert arr_multiply([0, 1, 2, 3]) == 0
    assert arr_multiply([-228.228, -1337, 3.14]) == 958142.22504
    assert arr_multiply([-1.1, -1]) == 1.1


# Тест функции, ищущей все чётные числа


def test_find_all_even():
    assert find_all_even([0, 1, 2, 3]) == [0, 2]
    assert find_all_even([-228.228, -1337, 3.14, 2]) == [2]
    assert find_all_even([-1.12, -1.05]) == []


# Псевдотест функции, считающей время скрипта для каждого файла


def test_script_time():
    for file_name in file_names:
        print("\n\033[34m{}".format(f"Время исполнения файла {file_name} - {script_time(file_name)}"))

