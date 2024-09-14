import unittest
from tests_12_3 import TournamentTest, RunnerTest

runST = unittest.TestSuite()

runST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)
