from Lesson_12_1 import Runner
import unittest
from Control import control_of_execution
# Изменяемые данные для теста
number = 10
compare_walk = 50
compare_run = 100




class RunnerTest(unittest.TestCase):
    is_frozen = False

    @control_of_execution
    def test_walk(self):
        resrun = Runner("Тест Walk")
        for _ in range(number):
            resrun.walk()
        self.assertEqual(resrun.distance, compare_walk)

    @control_of_execution
    def test_run(self):
        resrun = Runner("Тест Run")
        for _ in range(number):
            resrun.run()
        self.assertEqual(resrun.distance, compare_run)

    @control_of_execution
    def test_challenge(self):
        resrun = Runner("Runner")
        reswalk = Runner("Walker")

        for _ in range(number):
            resrun.run()
            reswalk.walk()

        self.assertNotEqual(resrun.distance, reswalk.distance)


if __name__ == '__main__':
    unittest.main()