

from asyncore import write
from encodings import utf_8
from fileinput import close


list=[] 
list_1=(input('Введите слово для игры: '))
for i in range(len(list_1)):
    list.append(list_1[i])
list_2=['а','д','е','л','а','и','д','а']
# with open ('Names.txt', 'r', encoding=utf_8):
for j in range(len(list_1)):
    if list[j]==list_2[5]:
        print('Аделаида')
# for j in range(len(list)):
#     if list[j]==list_2[5]:
#         print('Аделаида')
# for j in range(len(list)):
    
# path = 'Names.txt'
# data=open(path,'r', encoding='utf-8')
# for line in data:
#     if list.find(path)==True:
#         print(list.find(path))
#     # print(line)
# data.close()
# print(list.find(open('Names.txt','r')))
# print(len(list))

print(list)


