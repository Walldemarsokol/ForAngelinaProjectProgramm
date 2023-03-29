import random
from find_method import *


def test_3step(fact, list):
    F = []  # слово образованное в результате рандомного смешения букв
    Y = []  # список слов F
    check = 0
    while check < fact:
        random.shuffle(list)  # мешаем список
        F = (''.join(list))
        if F in Y:  # если "пар" есть в списке Y
            continue  # начнем мешать элементы списка сначала
        else:  # если не нашел
            Y[len(Y):] = [F]  # добавляем в конец списка  Y
            print(F)  # печатаем F, можно распечатать и пронумеровать элементы списка Y
            # file_list = find_method()
            # complete_method(file_list, F)
            # print(Y)
            check += 1
    return Y