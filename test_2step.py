import math
from test_3step import test_3step

def the_2nd_method(input_list, length):  # метод разбивает слово на маленькие слова последовательно от двух букв и более
    list_of_literals = []  # список для букв
    literals_check = 1  # старт для счетсика факториала
    list_of_words = [] # список для слов
    for i in range(length):  # пробегаемся по длине текста
        list_of_literals.append(input_list[i])  # создаетс список из букв
        factor = math.factorial(literals_check)  # факториал (максимум слов) создает ограничение по количеству слов
        literals_check += 1  # увеличение факториала для каждого следующего списка
        y = test_3step(factor, list_of_literals)  # создает списки слов из букв
        list_of_words.append(y)  # создает список списков слов
    return list_of_words

def run_method():
    word = input("Please, enter text: ")  # вводим текст, вводим в кавычках
    elements = list(word)  # преобразуем в список литералов
    length_list = len(elements)  # длина введенного текста(количество элементов списка) в int
    #y = (the_2nd_method(elements, length_list))
    wish_list = three_literals(elements,length_list)
    return wish_list

def three_literals(elements, length):
    some_word = []
    # print(elements)
    # print(length)
    second = 1
    for first_int in range(length):
        # print(first_int)
        for sec_int in range(second, length):
            for last_int in range(sec_int + 1, length):
                some_word.append(elements[first_int] + elements[sec_int] + elements[last_int])
        second+=1
        print(some_word)

    return some_word
