import logging


def try_except_(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            logging.info(f'{func.__name__} выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
        except Exception:
            logging.warning(f'ХЗ что такое')

    return wrapper


class Runner:
    @try_except_
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# class RunnerTest(unittest.TestCase):
#
#     is_frozen = False
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены' )
#     def test_walk(self):
#         a = Runner('vaasa')
#         for i in range(10):
#             a.walk()
#         self.assertEqual(a.distance, 50)
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_run(self):
#         a = Runner('vaasa_run')
#         for i in range(10):
#             a.run()
#         self.assertEqual(a.distance, 100)
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_challenge(self):
#         a = Runner('vaasa_run')
#         b = Runner('vaasa')
#         for i in range(10):
#             a.run()
#         for i in range(10):
#             b.walk()
#         self.assertNotEqual(b.distance, a.distance,'Не бегать')


first = Runner('Вося', 10)
second = Runner('Илья', -5)
third = Runner(52, 10)
#
# t = Tournament(101, first, second)
# print(t.start())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format="%(asctime)s|%(levelname)s|%(message)s")
