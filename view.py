

def menu() -> int:
    print('''Главное меню:\n
    1.Открыть файл
    2.Сохранитиь файл
    3.Показать контакты
    4.Создать контакт
    5.Изменить контакт
    6.Найти контакт
    7.Удалить контакт
    8.Выход''')
    while True:
        choice = input('Выберите пункт -> ')
        if choice.isdigit() and (0 < int(choice) < 9):
            return int(choice)


def show_contacts(pb: list[dict]):
    if pb == []:
        print('Телефонная книга пуста или файл не открыт.')
    else:
        for i, contact in enumerate(pb):
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{i+1}. {name:<20} {phone:<15} {comment:<15}')



def new_contact_input():
    name = input('Введите имя -> ')
    phone = input('Введите номер -> ')
    comment = input('Введите комментарий -> ')
    new_contact = {}
    new_contact['name'] = name
    new_contact['phone'] = phone
    new_contact['comment'] = comment
    print('Контакт добавлен!')
    return new_contact


def find_contact():
    find = input('Введите элемент для поиска -> ')   
    return find


def input_ind():
    ind = int(input('Введите номер контакта -> '))
    return ind
