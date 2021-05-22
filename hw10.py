from collections import UserDict


class Field:
	pass


class Name(Field):
	def __init__(self, name):
		self.name = name


class Phone(Field):
	def __init__(self, phone):
		self.phone = phone


class Record:
	def __init__(self, name):
		self.name = name
		self.phones = []

	def add_phone(self, phone):
		self.phones.append(phone)

	def remove_phone(self, phone):
		self.phones.remove(phone)

	def edit_phone(self, current_phone, new_phone):
		current_idx = self.phones.index(current_phone)
        self.phones[current_idx] = new_phone


class AdressBook(UserDict):
	def add_record(self, record):
		self.data[record] = record
