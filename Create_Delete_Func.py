from export_main import CreateTable




def writeFile(file_name):
    print('| Добавление нового контакта |\n')
    while True:
        with open(file_name, 'a', encoding='utf-8') as data:
            last_name = input('Фамилия: ')
            first_name = input('Имя: ')
            patronymic = input('Отчество: ')
            phone_number = input('Номер телефона: ')
            data.writelines(
                f'{last_name} {first_name} {patronymic} {phone_number}\n')
            choice = input(
                '\nНажмите Enter чтобы добавить новый контакт\nВведите 0 для выхода\n')
            if choice == '0':
                return




def DeleteContact(file_name):
    print('|      Удаление записи     |\n')
    while True:
        with open(file_name, 'r', encoding='utf-8') as data:
            line = data.readlines()

        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')

        deleted_str = int(
            input('Введите порядковый номер записи, который хотите удалить: '))
        del line[deleted_str - 1]

        with open(file_name, 'w', encoding='utf-8') as data:
            for i in line:
                data.write(i)
        choice = input(
            '\nНажмите Enter, чтобы продолжить удаление записей\nВведите 0 для выхода\n')
        if choice == '0':
            return