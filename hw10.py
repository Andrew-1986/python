from collections import UserDict


class Field:
	pass


class Name(Field):
	name = 'name'
	
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
		self.remove_phone(current_phone)
        	self.add_phone(new_phone)


class AdressBook(UserDict):
	def add_record(self, record):
		self.data[record] = record
