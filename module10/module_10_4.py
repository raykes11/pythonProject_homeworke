import queue
import threading
import time
from random import randint


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, names):
        self.names = names
        self.lock = threading.Lock()
        super().__init__()

    def run(self):
        time.sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.queue = queue.Queue()
        self.tables = list(args)

    def guest_arrival(self, *guests):
        guests = list(guests)
        for guest in guests:
            list_table = [table.guest for table in self.tables]
            if list_table.count(None) != 0:
                number_cell = list_table.index(None)
                self.tables[number_cell].guest = guest
                self.tables[number_cell].guest.start()
                print(f'{guest.names} сел(-а) за стол номер {self.tables[number_cell].number}.')
            else:
                self.queue.put(guest)
                print(f'{guest.names} в очереди')

    def discuss_guests(self):
        flag = True
        while flag:
            for eating in self.tables:
                list_table = [table.guest for table in self.tables]
                if None in list_table and not self.queue.empty():
                    number_cell = list_table.index(None)
                    table = self.tables[number_cell]
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(f'{table.guest.names} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                elif list_table.count(None) == len(self.tables) and self.queue.empty():
                    flag = False
                elif isinstance(eating.guest, type(None)):
                    pass
                elif not eating.guest.is_alive():
                    print(f'{eating.guest.names} покушал(-а) и ушёл(ушла)')
                    eating.guest = None


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra',
    '____Vitoria', '____Nikita', 'G___alina', 'Pa___vel', 'Il___ya', 'Alex____andra',
]

# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
