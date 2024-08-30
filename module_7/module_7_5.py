import os
import time

directory = os.getcwd()
for i in os.walk(directory):
    files = [f for f in os.listdir() if os.path.isfile(f)]
    for file in files:
        filepath = os.path.join(directory, file)
        formatted_time = time.ctime(os.path.getmtime(filepath))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(
            f'''Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, 
                Время изменения: {formatted_time}, Родительская директория: {parent_dir}''')
