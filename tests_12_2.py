import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.raner_1 = Runner('Усэйн', 10)
        self.raner_2 = Runner('Андрей', 9)
        self.raner_3 = Runner('Ник', 3)

    def str_(self, resault):
        for a in resault:
            resault[a] = str(resault[a])
        return resault

    #

    def test_first_run(self):
        first_run = Tournament(90, self.raner_1, self.raner_3)
        resault = first_run.start()
        if resault[len(resault)] == 'Ник':
            flag = True
        else:
            flag = False
        self.assertTrue(flag, '12345')
        resault = self.str_(resault)
        self.all_results[1] = resault

    def test_second_run(self):
        second_run = Tournament(90, self.raner_2, self.raner_3)
        resault = second_run.start()
        if resault[len(resault)] == 'Ник':
            flag = True
        else:
            flag = False
        self.assertTrue(flag, '12345')
        resault = self.str_(resault)
        self.all_results[2] = resault

    def test_third_run(self):
        self.raner_1 = Runner('Усэйн', 10)
        self.raner_2 = Runner('Андрей', 9)
        self.raner_3 = Runner('Ник', 3)
        third_run = Tournament(90, self.raner_3, self.raner_2, self.raner_1)
        resault = third_run.start()
        if resault[len(resault)] == 'Ник':
            flag = True
        else:
            flag = False
        self.assertTrue(flag, '12345')
        resault = self.str_(resault)
        self.all_results[3] = resault

    @classmethod
    def tearDownClass(self):
        for a in self.all_results:
            print(self.all_results.get(a))


def first_run(a, b):
    first_run = Tournament(90, a, b)
    resault = first_run.start()
    return resault


if __name__ == "__main__":
    unittest.main()
