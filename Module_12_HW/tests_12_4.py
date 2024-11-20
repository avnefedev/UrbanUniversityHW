from module_12_4 import Runner
import unittest
import logging


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            object = Runner('Вася', -5)
            for _ in range(10):
                object.walk()
            self.assertEqual(object.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            object = Runner(2, 5)
            for _ in range(10):
                object.run()
            self.assertEqual(object.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        object1, object2 = Runner('Вася'), Runner('Петя')
        for _ in range(10):
            object1.walk()
            object2.run()
        self.assertNotEquals(object1.distance, object2.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')

if __name__ == '__main__':
    unittest.main()



