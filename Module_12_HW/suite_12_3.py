import unittest
import tests_12_3

fullTestST = unittest.TestSuite()
fullTestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
fullTestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(fullTestST)
