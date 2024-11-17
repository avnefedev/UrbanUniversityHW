from module_12_1 import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Test walk"""
        object = Runner('Вася')
        for _ in range(10):
            object.walk()
        self.assertEqual(object.distance, 50)

    def test_run(self):
        """Test run"""
        object = Runner('Петя')
        for _ in range(10):
            object.run()
        self.assertEqual(object.distance, 100)

    def test_challenge(self):
        object1, object2 = Runner('Вася'), Runner('Петя')
        for _ in range(10):
            object1.walk()
            object2.run()
        self.assertNotEquals(object1.distance, object2.distance)


if __name__ == '__main__':
    unittest.main()



