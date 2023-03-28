
def find_method():#функция для поиска в текством файле
    text_list = ['test.txt']
    temp_list=[]
    for file in text_list:
        with open(file,'r',encoding= 'utf-8') as id:
            # for line in id:
            #     # if ';' in line:
            words = id.read().splitlines()
            # temp_list.append(id.read().splitlines())

    # print(temp_list)
    # print(words)
    return words


def complete_method(list,find_word):
    for line in list:
        if find_word == line: #.split('\n'):
                # print(line)
            print(f"Найдено слово:{find_word}")
            continue
        else:
                # print(line.strip())
            continue


# with open('numbers.txt', 'r') as f:
#     nums = f.read().splitlines()
# print(nums)
