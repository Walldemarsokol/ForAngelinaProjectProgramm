import random
from find_method import *
def the_3_step(fact,list,check):
    F=[] # слово образованное в результате рандомного смешения букв
    Y=[] #список слов F
    # temp_list = []
    while check<fact:
        random.shuffle(list) # мешаем список
        F=(''.join(list))
        if F in Y: # если "пар" есть в списке Y
            continue #начнем мешать элементы списка сначала
        else: #если не нашел
            Y[len(Y):]=[F]  #добавляем в конец списка  Y
            #print (F) #печатаем F, можно распечатать и пронумеровать элементы списка Y
            temp_list = find_method()
            # print(temp_list)
            # print(Y)
            # temp_list.append(F)

            complete_method(temp_list,F)
            check+=1
    return Y