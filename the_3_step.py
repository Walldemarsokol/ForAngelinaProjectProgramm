import random
from find_method import *
from find_word_function import *


def the_3_step(fact, list):
    F = []  # слово образованное в результате рандомного смешения букв
    Y = []  # список слов F
    check = 0
    count = 0
    while check < fact:
        random.shuffle(list)  # мешаем список
        F = (''.join(list))
        if F in Y:
            if count > 10000:
                break
            # если "пар" есть в списке Y
            else:
                count+=1
                continue  # начнем мешать элементы списка сначала
        else:  # если не нашел
            Y[len(Y):] = [F]  # добавляем в конец списка Y
            print(f'{F} = count{count}')  # печатаем F, можно распечатать и пронумеровать элементы списка Y
            find_in_dict(F)
            file_list = find_method()
            complete_method(file_list, F)
            # print(Y)
            check += 1
    return Y
