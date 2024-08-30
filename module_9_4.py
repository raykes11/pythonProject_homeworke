from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
compare = list(map(lambda x, y: x == y, first, second))
print(compare)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for line in data_set:
                file.write(f'{line}\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')

print()
print(first_ball())
print(first_ball())
print(first_ball())
