import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        a = Runner('vaasa')
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    def test_run(self):
        a = Runner('vaasa_run')
        for i in range(10):
            a.run()
        self.assertEqual(a.distance, 100)

    def test_challenge(self):
        a = Runner('vaasa_run')
        b = Runner('vaasa')
        for i in range(10):
            a.run()
        for i in range(10):
            b.walk()
        self.assertNotEqual(b.distance, a.distance, 'Не бегать')


if __name__ == "__main__":
    unittest.main()
