import math
from the_3_step import the_3_step

def the_2nd_method(input_list,length): # метод разбивает слово на маленькие слова последовательно от двух букв и более
    g=[]
    k=1
    L=[]
    for i in range(length): # пробегаемся по длине текста
        g.append(input_list[i]) # создаетс список из букв
        a=math.factorial(k) # факториал (максимум слов)
        k+=1  #
        z=0
        y=the_3_step(a,g,z)# создает списки слов из букв
        L.append(y)# создает список списков слов
    return L
    