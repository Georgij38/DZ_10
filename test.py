from main import *

book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

djohn_record = Record("DJohn")
djohn_record.add_phone("1234567890")
djohn_record.add_phone("5555555555")
book.add_record(djohn_record)

john = book.find("John")
print(john)
john.edit_phone("1234567890", "1112223333")
john.add_phone('1234567890')
book.book_print()




