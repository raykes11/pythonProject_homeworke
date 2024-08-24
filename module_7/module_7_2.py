def custom_write(file_name, *args):
    strings_positions = {}
    for arg in args:
        for string in arg:
            file = open(file_name, 'a', encoding='utf-8')
            byte_ = file.tell()
            file.write(f'{string}\n')
            file.close()
            file = open(file_name, 'r', encoding='utf-8')
            all_lines = file.readlines()
            lines = len(all_lines)
            file.close
            strings_positions[(lines, byte_)] = string
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
