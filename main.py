from collections import UserDict
from record import Record
import json


class AddressBook(UserDict):  # Клас для зберігання та управління записами.

    def add_record(self, obg_record):  # додає запис до self.data
        self.data[str(obg_record.name)] = obg_record

    def search_name(self, name):  # знаходить запис за ім'ям.
        for key, value in self.data.items():
            if str(key) == name:
                return value
        else:
            return 'there is no record'

    def search(self, part: str):  # пошук контактів по першим літерам або цифрам
        result = []
        if part.isalpha():
            for key in self.data:
                res = key.lower().strip().startswith(part.lower().strip())
                if res:
                    result.append(self.data[key])
                    return result
            else:
                print('contact not found')

        elif part.isdigit():
            for key, value in self.data.items():
                for phone in value.phone:
                    if phone.strip().startswith(part.strip()):
                        result.append(self.data[key])
                        return result
            else:
                print('contact not found')

        else:
            print(f'You have entered incorrect search parameters {part}')

    def delete(self, name):
        for key in self.data.keys():
            if str(key) == name:
                self.data.pop(key)
                break

    def book_print(self):
        for key, value in self.data.items():
            print(f'{key} : {value}')

    def iterator(self, batch_size=1):
        return self.AddressBookIterator(self, batch_size)

    def writing_file(self, file='contacts.json'): # запис до файлу
        with open(file, 'w') as write_contacts:
            json.dump(self.data, write_contacts, default=self._serialize_record, indent=1)

    def _serialize_record(self, obj):  # запис
        if isinstance(obj, Record):
            print({'name': obj.name, 'phone': obj.phone, 'birthday': obj.birthday})
            return {'name': obj.name, 'phone': obj.phone, 'birthday': obj.birthday}
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    def reading_file(self, file='contacts.json'): # зчітуваня з файлу
        with open(file, 'r') as read_contacts:
            loaded_data = json.load(read_contacts)
        for key, value in loaded_data.items():
            object = Record(value.get('name'))
            object.phone = value.get('phone')
            object.birthday = value.get('birthday')
            self.data[key] = object


    class AddressBookIterator:  # клас цо відповідае за ітерацію
        def __init__(self, address_book, batch_size):
            self.address_book = address_book
            self.__index = 0
            self.batch_size = batch_size

        def __iter__(self):
            return self

        def __next__(self):
            if self.__index >= len(self.address_book.data):
                raise StopIteration

            batch_end = min(self.__index + self.batch_size, len(self.address_book.data))
            batch = {
                key: self.address_book.data[key]
                for key in list(self.address_book.data.keys())[self.__index:batch_end]
            }
            self.__index += self.batch_size

            return batch
