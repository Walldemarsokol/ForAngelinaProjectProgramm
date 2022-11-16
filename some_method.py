import random
import math #подключение нужных модулей
from the_3_step import the_3_step

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
    the_3_step(a,G,z)
    # while z<a:
    #     print(f'check={z+1}')
    #     random.shuffle(G) # мешаем список
    #     F=(''.join(G))
    #     if F in Y: # если "пар" есть в списке Y
    #         continue #начнем мешать элементы списка сначала
    #     else: #если не нашел
    #         Y[len(Y):]=[F]  #добавляем в конец списка  Y
    #         print (F) #печатаем F, можно распечатать и пронумеровать элементы списка Y 
    #         z+=1