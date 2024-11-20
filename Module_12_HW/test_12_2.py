from module_12_2 import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_result.keys():
            print(cls.all_result[i])

    def test_1(self):
        test = Tournament(90, self.runner1, self.runner3)
        self.all_result['test1'] = test.start()
        self.assertTrue(self.all_result['test1'][max(self.all_result['test1'])] == 'Ник')

    def test_2(self):
        test = Tournament(90, self.runner2, self.runner3)
        self.all_result['test2'] = test.start()
        self.assertTrue(self.all_result['test2'][max(self.all_result['test2'])] == 'Ник')

    def test_3(self):
        test = Tournament(3, self.runner3, self.runner2, self.runner1)
        self.all_result['test3'] = test.start()
        self.assertTrue(self.all_result['test3'][max(self.all_result['test3'])] == 'Ник')


if __name__ == '__main__':
    unittest.main()



