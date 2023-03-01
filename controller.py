from view import menu, show_contacts, new_contact_input, find_contact, input_ind
import data

pb = data.PhoneBook('phone.txt')


def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                pb.open_file()
            case 2:
                pass
                pb.save()
            case 3:
                book = pb.get()
                show_contacts(book)
            case 4:
                new = new_contact_input()
                pb.add(new)
            case 5:
                book = pb.get()
                show_contacts(book)
                ind = input_ind()
                contact = new_contact_input()
                pb.change(ind, contact)

            case 6:
                find = find_contact()
                result = pb.find_o(find)
                show_contacts(result)
            case 7:
                book = pb.get()
                show_contacts(book)
                ind = input_ind()
                pb.delete(ind)
            case 8:
                print('До свидания!')
                break
