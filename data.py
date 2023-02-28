class PhoneBook:
    

    def __init__(self, path:str):
        self.phone_book = []
        self.path = path


    def open_file(self):
        file = open(self.path, 'r', encoding='UTF-8')
        data = file.readlines()
        for i in data:
            new = i.strip().split('-')
            contact = {}
            contact['name'] = new[0]
            contact['phone'] = new[1]
            contact['comment'] = new[2]
            self.phone_book.append(contact)
        print('Файл открыт!')
        file.close()


    def get(self):
        return self.phone_book


    def add(self, new_contact: list[dict]):
        self.phone_book.append(new_contact)


    def save(self):
       
        data = []
        for i in self.phone_book:
            new = '-'.join(i.values())
            data.append(new)
        data = '\n'.join(data)
        file = open(self.path, 'w', encoding='UTF-8')
        file.write(data)
        file.close


    def find_o(self, find_option: str):
        all_find = []
        for i in self.phone_book:
            for j in i.values():
                if find_option in j:
                    all_find.append(i)
        return all_find


    def change(self, ind: int, contact: dict):
        self.phone_book.pop(ind - 1)
        self.phone_book.insert(ind-1, contact)
        print('Контакт изменен!')


    def delete(self, ind):
        self.phone_book.pop(ind - 1)
        print('Контакт удален!')
