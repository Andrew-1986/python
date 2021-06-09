from collections import UserDict
from datetime import datetime
import pickle


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
        return self._value

    @value.setter
    def value(self, new_value):
        if self.new_value.isdigit():
        	self._value = new_value
        else:
            raise Exception("Please, enter a valid phone number")


class Birthday(Field):
    def __init__(self, birthday):
        self.birthday = birthday

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self.new_value.isdigit():
        	self._value = new_value
        else:
            raise Exception("Please, enter a valid birthday date")


class Record:
	def __init__(self, name, birthday=None):
		self.name = name
		self.phones = []
		self.birthday = birthday

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


class AdressBook(UserDict):
	def add_record(self, record):
		self.data[record] = record

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

    def serialize_data(self, file_name):
        with open(file_name, 'wb') as fh:
            pickle.dump(self, fh)

    def deserialize_data(self, file_name):
        with open(file_name, 'rb') as fh:
            result = pickle.load(fh)
        return result

    def find_contact(self, obj):
        self.result = []

        for key, value in self.data.items():
            if obj == key or obj in value:
                self.result.append(self.data[key])
        return self.result