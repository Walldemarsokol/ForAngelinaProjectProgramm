
import random
import math #подключение нужных модулей

L=input("enter text: ") # вводим текст, вводим в кавычках
D=list(L) # преобразуем в список
i=0 # счетчик  
Y=[] # пустой список
F=[]
l=len(D) # длина введенного текста(количество элементов списка)
l=math.factorial(l) # количество вариантов написания
while i<l: # делаем пока не исчерпаем все варианты
    print(f'check={i+1}')
    random.shuffle(D) # мешаем список
    F=(''.join(D)) # обедняем в один элемент (было ["п","а","р"] стало ["пар"]
    if F in Y: # если "пар" есть в списке Y
        continue #начнем мешать элементы списка сначала
    else: #если не нашел
        Y[len(Y):]=[F]  #добавляем в конец списка  Y
        print (F) #печатаем F, можно распечатать и пронумеровать элементы списка Y 
        i=i+1 #увеличиваем счетчик