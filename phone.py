from field import Field


class Phone(Field):
    def __init__(self, phone: str):
        self.value = phone # Викличемо сетер для валідації та зберігання значення



    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, phone):
        if phone .isdigit() and len(phone) == 10:
            Field.__init__(self, phone)
        else:
            raise ValueError('Phone number must contain 10 digits')

