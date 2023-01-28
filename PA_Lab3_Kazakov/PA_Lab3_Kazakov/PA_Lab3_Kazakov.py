import random
import linecache
import tkinter

main_file_path = "main_file.txt"
index_file_path = "index_file.txt"
rows_number = 1000
window = tkinter.Tk()
window.title("СУБД")
result_field = tkinter.Label(text="Тут будуть показані результати")
result_field.grid(row=0, column=0)

#Функція створення основного файлу
def create_main_file():
    main_file_data = []
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, rows_number):
        main_file_data.append((str(i)
                            + " "
                            + "".join([letters[random.randint(0, 25)] for j in range(0, 30)]))
                           + "\n")
    with open(main_file_path, "w") as file:
        for record in main_file_data:
            file.write(record)

#Функція створення файлу з індексною областю
def create_index_file():
    index_file = open(index_file_path, "w")
    for i in range(0, rows_number):
            with open(main_file_path, "r") as file:
                for j, content in enumerate(file):
                    value = int(content.split(" ")[0])
                    if i == value:
                        index_file.write(str(i) + " " + str(j) + "\n")
    return i

#Функція пошуку елемента
def element_search(row_id=None):
    comparisons_number = 0
    try:
        if not row_id:
            primary_key = int(entry_input_field.get())
        else:
            primary_key = row_id
    except:
        result_field.configure(text=f"Неправильний формат")
        return
    upper_index = rows_number
    lower_index = 0
    while lower_index <= upper_index:
        middle_index = (upper_index + lower_index) // 2
        value = linecache.getline(index_file_path, middle_index + 1)
        comparisons_number += 1
        if not value:
            result_field.configure(text=f"Елемент не знайдено \n Число порівнянь: {str(comparisons_number)}")
            return "Елемент не знайдено"
        if int(value.split(" ")[0]) == primary_key:
            result_field.configure(text=f"Рядок у базі даних знайдено \n Знайдений елемент: {linecache.getline(main_file_path, int(value.split(' ')[1]))} \n Число порівнянь: {str(comparisons_number)}")
            return value
        elif middle_index < primary_key:
            lower_index = middle_index + 1
        else:
            upper_index = middle_index - 1
    result_field.configure(text=f"Елемент не знайдено \n Число порівнянь: {str(comparisons_number)}")
    return "Елемент не знайдено"

#Функція додавання елемента
def element_add():
    global lines_number
    row = str(lines_number) + " " + " ".join(entry_input_field.get().split(" ")) + "\n"
    with open(main_file_path, "a+") as file:
        file.write(row)
        file.close()
    with open(index_file_path, "a+") as file1:
        file1.write(row.split(" ")[0] + " " + str(lines_number + 1) + "\n")
        file1.close()
    linecache.clearcache()
    lines_number += 1
    result_field.configure(text=f"Дані було успішно додано")
    print("Дані було успішно додано")
    return

#Функція видалення елементу
def element_delete():
    global lines_number
    try:
        row_id = int(entry_input_field.get())
        search_result = element_search(row_id).split(" ")
        index_value1 = int(search_result[0])
        index_value2 = int(search_result[1].replace("\n", ""))
        with open(index_file_path, "r+") as file:
            lines = []
            for index, line in enumerate(file):
                if int(line.split(" ")[0]) == index_value1:
                    lines.append("")
                else:
                    lines.append(line)
            file.write("")
        with open(index_file_path, "w") as file:
            file.writelines(lines)
        with open(main_file_path, "r+") as file1:
            lines = []
            for index, line in enumerate(file1):
                if index == index_value2-1:
                    lines.append("\n")
                else:
                    lines.append(line)
            file1.write("")
        with open(main_file_path, "w") as file1:
            file1.writelines(lines)
        print("Дані були успішно видалені")
        result_field.configure(text=f"Дані були успішно видалені")
        linecache.clearcache()
        lines_number -= 1
        return "Успіх!"
    except:
        result_field.configure(text=f"Неправильний формат")
        return

#Функція оновлення певного елементу
def element_update():
    try:
        global lines_number
        data = entry_input_field.get().split(" ")
        row_id = int(data[0])
        value = str(data[1])
        index_value = int(element_search(row_id).split(" ")[1].replace("\n", ""))
        with open(main_file_path, "r+") as file1:
            lines = []
            for index, line in enumerate(file1):
                if index == index_value-1:
                    lines.append(str(row_id) + " " + value + "\n")
                else:
                    lines.append(line)
            file1.write("")
            file1.close()
        with open(main_file_path, "w") as file1:
            file1.writelines(lines)
        print("База даних була оновлена")
        result_field.configure(text="База даних була оновлена")
        linecache.clearcache()
        return "Успіх!"
    except:
        result_field.configure(text="Неправильний формат")

#Основний код
create_main_file()#Створення основного файлу
lines_number = create_index_file() + 1
add_label = tkinter.Label(text="Додати елемент(формат: дані типу string без ключа)")
delete_label = tkinter.Label(text="Видалити елемент(формат: ключ елемента)")
search_label = tkinter.Label(text="Знайти елемент(формат: ключ елемента)")
update_label = tkinter.Label(text="Оновити елемент(формат: ключ елемента + пробіл + оновлені дані)")
entry_input_field = tkinter.Entry()
add_button = tkinter.Button(text="Додати", command=element_add)
delete_button = tkinter.Button(text="Видалити", command=element_delete)
search_button = tkinter.Button(text="Знайти", command=element_search)
update_button = tkinter.Button(text="Оновити", command=element_update)
add_button.grid(row=2, column=1)
add_label.grid(row=2, column=0)
delete_button.grid(row=3, column=1)
delete_label.grid(row=3, column=0)
search_button.grid(row=4, column=1)
search_label.grid(row=4, column=0)
update_button.grid(row=5, column=1)
update_label.grid(row=5, column=0)
entry_input_field.grid(row=1, column=0)
window.mainloop()