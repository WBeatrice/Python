# Задача №49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или 
# фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

from os import path

file_base = "base.txt"
last_id = 0
all_info = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass



def read_records():
    global all_data, last_id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])

        return all_data

def show_all():
    if all_info:
        print(*all_info, sep="\n")
    else:
        print("Empty data")

def add_new_contact():
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""
    for i in array:
        string += input(f"Enter {i} ") + " "
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")
    
def search_by_record():
    search = Existing_Contact(0, input("Enter a search query: "))
    if search:
        print(*search, sep="\n")
    else:
        print("Incorrect request! Try again")
      
def Existing_Contact(id, info):
    if id:
        new_contact = [i for i in all_info if id in i.split()[0]]
    else:
        new_contact = [i for i in all_info if info in i]
    return new_contact

def Deletion():
    global all_info
    lines = "\n"
    show_all()
    delete = input("Enter a deletion request: ")

    if Existing_Contact(delete, ""):
        all_info = [i for i in all_info if i.split()[0] != delete]
        
        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{lines.join(all_info)}\n')
        print("The information has been deleted!\n")
    else:
        print("Incorrect request! Try again\n")

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n" #Показать все записи
                       "2. Add a record\n" #Добавьте запись
                       "3. Search a record\n" #Выполните поиск по записи
                       "4. Change\n" #Измените
                       "5. Delete\n" #Удалить
                       "6. Exp/Imp\n" #Опыт/Imp
                       "7. Exit\n") #Выход
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_by_record()
            case "4":
                pass
            case "5":
                Deletion()
            case "6":
                pass
            case "7":
                play = False
            case _: #ошибка при вводе неправильных сибволов
                print("Try again!\n")


main_menu()