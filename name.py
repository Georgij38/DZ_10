from field import Field



class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)

    @property
    def name(self):
        return self._value

    @name.setter
    def name(self, new_name):
        self._value = new_name

