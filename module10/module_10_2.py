import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        self.names = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.names}, на нас напали!')
        evel = 100
        day = 0
        while evel > 0:
            evel = evel - self.power
            day += 1
            if evel < 0:
                evel = 0
            print(f'{self.names} сражается {day} день(дня)..., осталось {evel} воинов.')
            time.sleep(1)
        print(f'{self.names} одержал победу спустя {day} дней(дня)!')


class Castle:
    def __init__(self, *knight):
        self.knight = list(knight)
        print(self.knight)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
