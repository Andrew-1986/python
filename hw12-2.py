from collections import UserDict
from datetime import datetime
import pickle
import sys
import os.path

'''Classess'''
class Field:
	def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
	filed_name = "name"

	def __init__(self, name):
		self.name = name


class Phone(Field):
	def __init__(self, phone):
		self.phone = phone

	@property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if self.new_value.isdigit():
        	self.__value = new_value
        else:
            raise Exception("Please, enter a valid phone number")


class Birthday(Field):
    def __init__(self, birthday):
        self.birthday = birthday

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if self.new_value.isdigit():
        	self.__value = new_value
        else:
            raise Exception("Please, enter a valid birthday date")


class Record:
	def __init__(self, name, birthday=None):
		self.name = name
		self.phones = []
		self.birthday = birthday

	def __str__(self):
        result = ""
        result += f"name: {self.name.value}"

        if self.birthday:
            result += f"birthday: {str(self.birthday.value)} "
        result += f"phones - {', '.join([phone.value for phone in self.phones])}"

        return result

	def add_phone(self, phone):
		self.phones.append(phone)

	def remove_phone(self, phone):
		self.phones.remove(phone)

	def edit_phone(self, current_phone, new_phone):
		current_idx = self.phones.index(current_phone)
        self.phones[current_idx] = new_phone

    def days_to_birthday(self):
    	if self.birthday: 
        	current_day = datetime.now()
        	current_year = current_day.year
            b_day = self.birthday.replace(current_year)
            delta = abs(b_day - current_day)

            return delta
        else:
            raise Exception("Please, add a birthday date")

    def change_birthday(self,  new_birthday):
        if new_birthday.value != None:
            self.birthday = new_birthday
        else:
            raise Exception("New birthday is not correct")


class AdressBook(UserDict):
	def add_record(self, record):
		self.data[record.name] = record

    def __next__(self):
        counter = 0

        for key, value in self.data.items():
            if counter >= len(self):
            	raise StopIteration
            else:
                return (key, value)
                counter += 1

    def __iter__(self):
        self.number = 0
        return self

    def find_contact(self, contacts):
        result = []

        if self.name.find(contacts) != -1 or self.phone.find(contacts) != -1:
        	result.append(self.name)
        	
        return result


'''Bot part'''
'''error decorator'''
def input_error(func):
    def inner(data):
        try:
            result = func(data)
            return result
        except Exception as error:
            print("Error:", error)
        else:
            return result
    return inner


'''input functions'''
@input_error
def hello(data):
    return "How can I help you?"


@input_error
def add_phone(data):
    data = data.replace('Add phone ', '')
    if len(data.split()) == 2:
        name, phone = data.split()

        if name not in address_book:
            address_book.add_record(Record(name=Name(name), phone=Phone(phone)))
        else:
            phone = Phone(phone)
            address_book[name].add_phone(phone)
    else:
        raise Exception("Enter a data(name, phone) please")


@input_error
def show_phone(data):
    data = data.replace('phone ', '')
    if len(data.split()) == 1:
        name = data
        if name in address_book:
            return address_book[name]
        else:
            raise Exception("Abonent is not found")
    else:
        raise Exception("Enter a name")


@input_error
def change_phone(data):
    data = data.replace('Change phone ', '')
    if len(data.split()) == 3:
        name, phone, new_phone = data.split()
        if name in address_book:
            address_book[name].edit_phone(Phone(phone), Phone(new_phone))
        else:
            raise Exception("Abonent is not found")
    else:
        raise Exception("Enter a data(name, phone) please")


@input_error
def add_birthday(data):
    data = data.replace('Add birthday ', '')

    if len(data.split()) == 2:
        name, birthday = data.split()
        birthday = Birthday(birthday)

        if name not in address_book:
            address_book.add_record(Record(name=Name(name), birthday=birthday))
        elif address_book[name].birthday.value == None:
            address_book[name].change_birthday(birthday)
        else:
            raise Exception("Birthday date is find")
    else:
        raise Exception("Enter a data(name, birthday) please")


@input_error
def find_data(data):
    data = data.replace('find ', '')
    if len(data.split()) == 1:
        result = address_book.find_contact(data)
        return result


@input_error
def show_all(data):
    data = data.replace('show all', '')

    if len(data.split()) == 1:
        try:
            i = int(data)
        except:
            i = 1
    else:
        i = len(address_book.data)

    for element in address_book.iterator(i):
        print(element)


@input_error
def bye(data):
	with open(file_name, 'wb') as fh:
        pickle.dump(address_book, fh)

    return "Good bye!"


@input_error
def ext(data):
    return 'break'


'''handlers'''
HANDLERS = {
    "hello" : hello,
    "good bye": bye,
    "close": bye,
    "exit": bye,
    "add phone" : add_phone,
    "add birthday": add_birthday,
    "change" : change_phone,
    "phone" : show_phone,
    "show all" : show_all,
    "find data": find_data,
    ".": ext
}


'''action function'''
@input_error
def action(data):
    for cmd in HANDLERS:
        if data.startswith(cmd):
            return HANDLERS[cmd]
    raise Exception("This is an uncorrect command! Please restart programm and enter one of the commands(hello, add, change, phone, show all, good bye, close or exit.)")


if __name__ == '__main__':
	address_book = AddressBook()

	if os.path.isfile(file_name):
        with open(file, 'rb') as fh:
            address_book = pickle.load(fh)

    while True:
        data = input("Enter a command: ")

        func = action(data)
        if isinstance(func, Exception):
            print(func)
            continue

        result = func(data)
        if result == 'break':
            break
        elif result:
            print(result)
        if result == 'Good bye!':
            break
