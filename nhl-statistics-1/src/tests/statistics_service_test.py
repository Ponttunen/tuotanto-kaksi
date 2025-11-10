"""Module for testing StatisticsService"""

import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub: # [too-few-public-methods]
    """Class for teststub that we do not need to use the real deal which
    fetches the data from the net."""
    def get_players(self):
        """Method returns a bunch of dummy Players."""
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    """StatisticsService's testclass"""
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_name(self):
        """Tests search-method, mathcing case."""
        self.assertEqual(str(self.stats.search("Semenko")), str(Player("Semenko", "EDM", 4, 12)))

    def test_search_doesnt_find_a_name(self):
        """Tests search-method, not a mathcing case."""
        self.assertEqual(str(self.stats.search("Samenko")), "None")

    def test_team_finds_names(self):
        """Tests team-method, finds players -case."""
        self.assertEqual(str(self.stats.team("EDM")[0]), str(Player("Semenko", "EDM", 4, 12)))
        self.assertEqual(str(self.stats.team("EDM")[1]), str(Player("Kurri",   "EDM", 37, 53)))
        self.assertEqual(str(self.stats.team("EDM")[2]), str(Player("Gretzky", "EDM", 35, 89)))

    def test_top(self):
        """Tests top-method, 3-best -case."""
        self.assertEqual(str(self.stats.top(3)[0]), str(Player("Gretzky", "EDM", 35, 89)))
        self.assertEqual(str(self.stats.top(3)[1]), str(Player("Lemieux", "PIT", 45, 54)))
        self.assertEqual(str(self.stats.top(3)[2]), str(Player("Yzerman", "DET", 42, 56)))
