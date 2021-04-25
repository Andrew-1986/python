import pathlib
import sys
import shutil
import re


def normalize():
    symbols = ("абвгдеёзийклмнопрстуфхъыьэАБВГДЕЁЗИЙКЛМНОПРСТУФХЪЫЬЭ",
               "abvgdeezijklmnoprstufh'y'eABVGDEEZIJKLMNOPRSTUFH'Y'E")

    compare_symbols = {ord(a):ord(b) for a, b in zip(*symbols)}

    text = input("Введите текст: " )
    text = text.translate(compare_symbols)
    text = re.sub(r'\W', '_', text)

    return text


def sort_files():
	if len(sys.argv) < 2:
		user_input = ""
	else:
		user_input = sys.argv[1]

	path = pathlib.Path(user_input)

	if path.exists():
		if path.is_dir():
			for files in Path(path).glob("*.png", "*.svg", "*.jpg", "*.jpeg"):
				file_suffix = files.suffix
    			file_name = files.rsplit(".", 1)[0]
    			new_file_name = normalize(filename)
    			source_path = f'{path}/{files}'
				destination_path = f'{path}/images/{new_file_name}.{file_suffix}'
    			shutil.move(source_path, destination_path)
			for files in Path(path).glob("*.avi", "*.mp4", "*.mov", "*.mkv"):
    			file_suffix = files.suffix
    			file_name = files.rsplit(".", 1)[0]
    			new_file_name = normalize(filename)
    			source_path = f'{path}/{files}'
				destination_path = f'{path}/video/{new_file_name}.{file_suffix}'
    			shutil.move(source_path, destination_path)
    		for files in Path(path).glob("*.doc", "*.txt", "*.pdf", "*.docx"):
    			file_suffix = files.suffix
    			file_name = files.rsplit(".", 1)[0]
    			new_file_name = normalize(filename)
    			source_path = f'{path}/{files}'
				destination_path = f'{path}/documents/{new_file_name}.{file_suffix}'
    			shutil.move(source_path, destination_path)
    		for files in Path(path).glob("*.mp3", "*.ogg", "*.wav", "*.arm"):
    			file_suffix = files.suffix
    			file_name = files.rsplit(".", 1)[0]
    			new_file_name = normalize(filename)
    			source_path = f'{path}/{files}'
				destination_path = f'{path}/music/{new_file_name}.{file_suffix}'
    			shutil.move(source_path, destination_path)
    		for files in Path(path).glob("*.zip", "*.gz", "*.tar"):
    			archives.append(files)
    			archive_format = files.suffix
    			archive_path = f'{path}/archives/{archive_format}'
    			shutil.unpack_archive(files, archive_path, archive_format)
		else:
			print(f"{path} is not dir")
	else:
		print(f"{path.absolute()} not exists")


if __name__ == '__main__':
	print(sort_files())