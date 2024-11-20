from module_12_2 import Tournament, Runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Ghjql')
    def test_walk(self):
        object = Runner('Вася')
        for _ in range(10):
            object.walk()
        self.assertEqual(object.distance, 50)

    @unittest.skipIf(is_frozen, 'Ghjql')
    def test_run(self):
        object = Runner('Петя')
        for _ in range(10):
            object.run()
        self.assertEqual(object.distance, 100)

    @unittest.skipIf(is_frozen, 'Ghjql')
    def test_challenge(self):
        object1, object2 = Runner('Вася'), Runner('Петя')
        for _ in range(10):
            object1.walk()
            object2.run()
        self.assertNotEquals(object1.distance, object2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_result.keys():
            print(cls.all_result[i])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        test = Tournament(90, self.runner1, self.runner3)
        self.all_result['test1'] = test.start()
        self.assertTrue(self.all_result['test1'][max(self.all_result['test1'])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        test = Tournament(90, self.runner2, self.runner3)
        self.all_result['test2'] = test.start()
        self.assertTrue(self.all_result['test2'][max(self.all_result['test2'])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        test = Tournament(3, self.runner3, self.runner2, self.runner1)
        self.all_result['test3'] = test.start()
        self.assertTrue(self.all_result['test3'][max(self.all_result['test3'])] == 'Ник')


if __name__ == '__main__':
    unittest.main()



