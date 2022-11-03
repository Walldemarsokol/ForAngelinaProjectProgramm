

from encodings import utf_8


list=[] 
list_1=(input('Введите слово для игры: '))
for i in range(len(list_1)):
    list.append(list_1[i])
list_2=['а','д','е','л','а','и','д','а']
with open ('Names.txt', 'r', encoding=utf_8):
    for j in range(len(list_1)):
        if list[j]==list_2[5]:
            print('Аделаида')



