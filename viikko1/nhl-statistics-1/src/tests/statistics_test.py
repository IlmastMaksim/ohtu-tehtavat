import unittest
from statistics import Statistics, sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_finding_player(self):
        player = Player("Semenko", "EDM", 4, 12)
        result = self.statistics.search(player.name)
        self.assertEqual(result.name, player.name)

    def test_checking_if_none_is_returned_for_wrong_player(self):
        player = Player("Name", "CNN", 11, 11)
        result = self.statistics.search(player.name)
        self.assertTrue(result == None)

    def test_checking_points(self):
        player = Player("Semenko", "EDM", 4, 12)
        points = sort_by_points(player)
        self.assertAlmostEqual(points, 16)

    def test_checking_team_filtering(self):
        team = [Player("Semenko", "EDM", 4, 12),
                    Player("Kurri", "EDM", 37, 53), 
                    Player("Gretzky", "EDM", 35, 89)]
        found_team = self.statistics.team("EDM")
        self.assertEqual(found_team[0].name, team[0].name)
        self.assertEqual(found_team[1].name, team[1].name)
        self.assertEqual(found_team[2].name, team[2].name)

    def test_checking_best_players(self):
        best_players = [Player("Gretzky", "EDM", 35, 89), 
                Player("Lemieux", "PIT", 45, 54),
                Player("Yzerman", "DET", 42, 56)]
        found_best_players = self.statistics.top_scorers(2)
        self.assertEqual(found_best_players[0].name, best_players[0].name)
        self.assertEqual(found_best_players[1].name, best_players[1].name)
        self.assertEqual(found_best_players[2].name, best_players[2].name)