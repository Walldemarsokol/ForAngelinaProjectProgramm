import random

def the_3_step(fact,list):
    F=[]
    Y=[]
    z=1 #счетчик для метода
    while z<fact:
            random.shuffle(list) # мешаем список
        # random.shuffle(D)  # мешаем список
        # F=(''.join(D)) # объединяем в один элемент (было ["п","а","р"] стало ["пар"])
            F=(''.join(list))
            if F in Y: # если "пар" есть в списке Y
                z+=1
                continue #начнем мешать элементы списка сначала
            else: #если не нашел
                Y[len(Y):]=[F]  #добавляем в конец списка  Y
                print (Y)
    return Y