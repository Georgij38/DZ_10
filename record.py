from name import Name
import datetime
from phone import Phone
from birthday import Birthday

class Record:  # Клас для зберігання інформації про контакт
    def __init__(self, name: str, birthday=''):
        self._name = Name(name)
        self.birthday = birthday
        self._phones = []

    def days_to_birthday(self):  # повертає кількість днів до наступного дня народженя
        current_date = datetime.now()
        next_birthday = datetime(current_date.year, self._birthday._value.month, self._birthday._value.day)
        if current_date > next_birthday:
            next_birthday = datetime(current_date.year + 1, self._birthday._value.month, self._birthday._value.day)
        days_left = (next_birthday - current_date).days

        print(f"До наступного дня народження залишилося {days_left} днів.")
        return days_left

    def __str__(self):
        return f"Contact name: {self._name._value}, phones: {'; '.join(p._value for p in self._phones)}, birthday: {self._birthday}"


    @property
    def birthday(self):
        return str(self._birthday)

    @birthday.setter
    def birthday(self, date):
        self._birthday = Birthday(date)

    @property
    def name(self):
        return self._name._value

    @name.setter
    def name(self, new_name):
        self._name = Name(new_name)

    def search_phone(self, phone):  # пошук
        for el in self._phones:
            if str(el) == phone:
                return el

    def remove_phone(self, phone):  # Видалиня
        self._phones.remove(self.search_phone(phone))

    def change_phone(self, phone, new_phone):  # редагуваня
        phone_obg = self.search_phone(phone)
        self._phones[self._phones.index(phone_obg)] = Phone(new_phone)

    @property
    def phone(self):
        result = []
        for el in self._phones:
            result.append(str(el))
        return result

    @phone.setter
    def phone(self, phone):
        try:
            if isinstance(phone, str):
                self._phones.append(Phone(phone))
            elif isinstance(phone, list):
                self._phones.extend([Phone(p) for p in phone])
        except ValueError as error:
            print(error)

