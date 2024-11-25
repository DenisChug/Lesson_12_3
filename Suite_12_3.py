import unittest

from TestRunner import RunnerTest
from TournamentTest import TournamentTest

suite = unittest.TestSuite()

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)