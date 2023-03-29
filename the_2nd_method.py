import math
from the_3_step import the_3_step


def the_2nd_method(input_list, length):  # метод разбивает слово на маленькие слова последовательно от двух букв и более
    list_of_literals = []  # список для букв
    literals_check = 1  # старт для счетсика факториала
    list_of_words = [] # список для слов
    for i in range(length):  # пробегаемся по длине текста
        list_of_literals.append(input_list[i])  # создаетс список из букв
        factor = math.factorial(literals_check)  # факториал (максимум слов) создает ограничение по количеству слов
        literals_check += 1  # увеличение факториала для каждого следующего списка
        y = the_3_step(factor, list_of_literals)  # создает списки слов из букв
        list_of_words.append(y)  # создает список списков слов
    return list_of_words
