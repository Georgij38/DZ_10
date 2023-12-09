from collections import UserDict


class Field:  # Базовий клас для полів запису. Буде батьківським для всіх полів,
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):  # Клас для зберігання імені контакту. Обов'язкове поле
    pass
    # реалізація класу


# Клас для зберігання номера телефону.
# Має валідацію формату (10 цифр).
# Необов'язкове поле з телефоном та таких один запис Record може містити декілька.
class Phone(Field):
    def __init__(self, value):
        super().__init__(self.validate(value))

    @staticmethod
    def validate(value):
        if value.isdigit() and len(value) == 10:
            return value
        else:
            raise ValueError


class Birthday(Field):
    pass


class Record:  # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):  # пошук
        for el in self.phones:
            if str(el) == phone:
                return el

    def remove_phone(self, phone):  # Видалиня
        self.phones.remove(self.find_phone(phone))

    def edit_phone(self, phone, new_phone):  # редагуваня
        phone_obg = self.find_phone(phone)
        self.phones[self.phones.index(phone_obg)] = Phone(new_phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):  # Клас для зберігання та управління записами.

    def add_record(self, obg_record):  # додає запис до self.data
        self.data[str(obg_record.name)] = obg_record

    def find(self, name):  # знаходить запис за ім'ям.
        for key, value in self.data.items():
            if str(key) == name:
                return value

    def delete(self, name):
        for key in self.data.keys():
            if str(key) == name:
                self.data.pop(key)
                break

    def book_print(self):
        for key, value in self.data.items():
            print(f'{key} : {value}')
