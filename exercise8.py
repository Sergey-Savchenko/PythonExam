import json
from datetime import date

def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ';')
            data_array.append(item)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ';'.join(i)
            data.write(f'{write_element}\n')

def add_item(filename, today = '', head = '', notion = ''):
    data_array = read_file(filename) 
    max_id = 0
    for i in range(0,len(data_array)):
        if max_id < int(data_array[i][0]): 
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    print(next_id)
    head = input('Head: ')
    notion = input('Notion: ')
    new_item = []
    new_item.append(str(next_id))
    today = date.today()
    new_item.append(str(today))
    new_item.append(head)
    new_item.append(notion)
    # print(new_item)
    # print(data_array)
    data_array.append(new_item)
    # print(data_array)
    write_file(filename, data_array)

def show_all_items(filename):
    data_array = read_file(filename)    
    for i in range(0,len(data_array)):
        print("ID: ", data_array[i][0], "Дата: ", data_array[i][1], "Заголовок: ", data_array[i][2], "Заметка: ", data_array[i][3])

# Добавил функцию поиска по id
def search_id(number,data_array):
    number = str(number)
    for i in range(0,len(data_array)):
        if number==data_array[i][0]:
            # print(data_array[i][0])
            # print(i)
            return i

# Функция замены данных
def change_item(filename):
    data_array = read_file(filename)
    change_id = int(search_id(int(input('Введите номер записи для изменения: ')), data_array))
    head = input('Head: ')
    notion = input('Notion: ')
    # data_array[search_id][0] = str(search_id)
    today = date.today()
    data_array[change_id][1] = str(today)
    data_array[change_id][2] = head
    data_array[change_id][3] = notion
    # print(data_array)
    write_file(filename, data_array)

# Функция удаления данных
def delete_item(filename):
    data_array = read_file(filename)
    destroy_id = int(search_id(int(input('Введите номер записи для удаления: ')), data_array))
    data_array.pop(destroy_id)
    # print(data_array)
    write_file(filename, data_array)

def show_one_item(filename):
    data_array = read_file(filename)
    show_id = int(search_id(int(input('Введите номер записи для просмотра: ')), data_array))    
    print("ID: ", data_array[show_id][0], "Дата: ", data_array[show_id][1], "Заголовок: ", data_array[show_id][2], "Заметка: ", data_array[show_id][3])

def show_time_item(filename):
    data_array = read_file(filename)
    show_id = str(input('Введите дату записи для просмотра: '))
    for i in range(0,len(data_array)):
        if show_id==data_array[i][1]:
            print("ID: ", data_array[i][0], "Дата: ", data_array[i][1], "Заголовок: ", data_array[i][2], "Заметка: ", data_array[i][3])

def menu():
    print('Welcome to Notion!')
    print('1 - Посмотреть все заметки')
    print('2 - Добавить заметку')
    print('3 - Изменить заметку')
    print('4 - Удалить заметку')
    print('5 - Показать заметку по номеру')
    print('6 - Показать заметки по дате')
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2: 
        add_item(filename)
    elif user_operation == 3: 
        change_item(filename)
    elif user_operation == 4: 
        delete_item(filename)
    elif user_operation == 5: 
        show_one_item(filename)
    elif user_operation == 6: 
        show_time_item(filename)

filename = 'notion.json'
menu()