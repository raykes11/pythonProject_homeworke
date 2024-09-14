import unittest

from tests_12_2 import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        a = Runner('vaasa')
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        a = Runner('vaasa_run')
        for i in range(10):
            a.run()
        self.assertEqual(a.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        a = Runner('vaasa_run')
        b = Runner('vaasa')
        for i in range(10):
            a.run()
        for i in range(10):
            b.walk()
        self.assertNotEqual(b.distance, a.distance, 'Не бегать')


class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_run(self):
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


if __name__ == "__main__":
    unittest.main()
