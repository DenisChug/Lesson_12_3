import unittest
from Lesson_12_2 import Runner, Tournament
from Control import control_of_execution

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.athlete1 = Runner("Усэйн", 10)
        self.athlete2 = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            formatted_result = cls.format_results(result)
            print(formatted_result)

    @staticmethod
    def format_results(results):
        formatted = ("{" + ", ".join([f"{place}: {runner}" for place, runner in results.items()]) + "}")
        return formatted

    @control_of_execution
    def test_athlete1_and_nick(self):
        tournament = Tournament(90, self.athlete1, self.nick)
        results = tournament.start()
        TournamentTest.all_results["test_athlete1_and_nick"] = results

        last_runner_name = results[max(results.keys())].name
        self.assertTrue(last_runner_name == "Ник", f"Ожидался Ник, а был {last_runner_name}")

    @control_of_execution
    def test_athlete2_and_nick(self):
        tournament = Tournament(90, self.athlete2, self.nick)
        results = tournament.start()
        TournamentTest.all_results[f"Тест {self.athlete2} и {self.nick}"] = results

        last_runner_name = results[max(results.keys())].name
        self.assertTrue(last_runner_name == "Ник", f"Ожидался Ник, а был {last_runner_name}")

    @control_of_execution
    def test_athlete1_athlete2_and_nick(self):
        tournament = Tournament(90, self.athlete1, self.athlete2, self.nick)
        results = tournament.start()
        TournamentTest.all_results[f"Тест {self.athlete1} и {self.nick}"] = results

        last_runner_name = results[max(results.keys())].name
        self.assertTrue(last_runner_name == "Ник", f"Ожидался Ник, а был {last_runner_name}")


if __name__ == "__main__":
    unittest.main()