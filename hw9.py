USERS = {}


'''error decorator'''
def input_error(func):
    def inner(data):
        try:
            result = func(data)
            return result
        except KeyError:
            print("No user with given name")
        except ValueError:
            print("Give me name and phone please")
        except IndexError:
            print("Give me name and phone please")
    return inner


'''input functions'''
@input_error
def hello(data):
    return "How can I help you?"


@input_error
def add_phone(data):
    name, phone = data[0], data[1]
    USERS[name] = phone
    return f'The user {name} was added!'


@input_error
def change_phone(data):
    name, phone = data[0], data[1]
    for key in USERS.keys():
        if key == name:
            USERS[key] = phone
    return f'The phone number for {name} was changed!'


@input_error
def show_phone(data):
    return USERS[data[0]]


@input_error
def show_all(data):
    for name, phone in USERS.items():
        return f'{name} - {phone}'


@input_error
def bye(data):
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
    "add" : add_phone,
    "change" : change_phone,
    "phone" : show_phone,
    "show all" : show_all,
    ".": ext
}


'''action function'''
def action(data):
    for cmd in HANDLERS:
        if data.startswith(cmd):
            return HANDLERS[cmd]
    raise Exception("This is an uncorrect command! Please restart programm and enter one of the commands(hello, add, change, phone, show all, good bye, close or exit.)")


def main():
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


if __name__ == '__main__':
    main()