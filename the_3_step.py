import random

def the_3_step(fact,list,check):
    F=[]
    Y=[]
    while check<fact:
        random.shuffle(list) # мешаем список
        F=(''.join(list))
        if F in Y: # если "пар" есть в списке Y
            continue #начнем мешать элементы списка сначала
        else: #если не нашел
            Y[len(Y):]=[F]  #добавляем в конец списка  Y
            print (F) #печатаем F, можно распечатать и пронумеровать элементы списка Y 
            check+=1
            
    return Y