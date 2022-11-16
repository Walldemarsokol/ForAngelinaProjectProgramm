import random
import math #подключение нужных модулей

L=input("enter text: ") # вводим текст, вводим в кавычках
D=list(L) # преобразуем в список
i=0 # счетчик

k=1

Y=[] # пустой список
F=[]
G=[]
l=len(D) # длина введенного текста(количество элементов списка)

for i in range(l): # делаем пока не исчерпаем все варианты
    G.append(D[i])
    print(f'check I ={i+1}')
    print(G)
    a=math.factorial(k)
    print(f'factorial={a}')
    k+=1
    z=0
    while z<a:
        print(f'check={z+1}')
        random.shuffle(G) # мешаем список
        # random.shuffle(D)  # мешаем список
        # F=(''.join(D)) # объединяем в один элемент (было ["п","а","р"] стало ["пар"])
        F=(''.join(G))
        if F in Y: # если "пар" есть в списке Y
            continue #начнем мешать элементы списка сначала
        else: #если не нашел
            Y[len(Y):]=[F]  #добавляем в конец списка  Y
            print (F) #печатаем F, можно распечатать и пронумеровать элементы списка Y 
            z+=1
    
    # while k<j:
    #     # l=math.factorial(l) # количество вариантов написания
    #     a=math.factorial(k)
    #     print(a)
    #     k+=1
        
    #             # i=i+1 #увеличиваем счетчик
    #             # k+=1
    #             # z+=1
    #             # j+=1