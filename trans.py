import re


def normalize():
    symbols = ("абвгдеёзийклмнопрстуфхъыьэАБВГДЕЁЗИЙКЛМНОПРСТУФХЪЫЬЭ",
               "abvgdeezijklmnoprstufh'y'eABVGDEEZIJKLMNOPRSTUFH'Y'E")

    compare_symbols = {ord(a):ord(b) for a, b in zip(*symbols)}

    text = input("Введите текст: " )
    text = text.translate(compare_symbols)
    text = re.sub(r'\W', '_', text)

    return text


if __name__ == '__main__':
    print(normalize())