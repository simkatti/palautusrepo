import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12), #16
            Player("Lemieux", "PIT", 45, 54), #99
            Player("Kurri",   "EDM", 37, 53), #90
            Player("Yzerman", "DET", 42, 56), #98
            Player("Gretzky", "EDM", 35, 89) #124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_player(self):
        player = self.stats.search("Kurri")

        self.assertIsNotNone(player) 
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)

    def test_no_player_found(self):
        player = self.stats.search("Messi")

        self.assertIsNone(player)

    def test_team_players(self):
        players = self.stats.team("EDM")

        for p in players:
            self.assertEqual(p.team, "EDM")

        self.assertEqual(len(players), 3)

    def test_returns_top_players_by_points(self):
        top_3 = self.stats.top(3, SortBy.POINTS)

        top_players=["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]

        i = 0
        for player in top_3:
            self.assertEqual(player.name, top_players[i])
            i += 1
    def test_returns_top_players_by_goals(self):
        top_3 = self.stats.top(3, SortBy.GOALS)

        top_players = ["Lemieux","Yzerman","Kurri","Gretzky","Semenko"]

        i = 0
        for player in top_3:
            self.assertEqual(player.name, top_players[i])
            i += 1

    def test_returns_top_players_by_assists(self):
        top_3 = self.stats.top(3, SortBy.ASSISTS)

        top_players = ["Gretzky","Yzerman","Lemieux","Kurri","Semenko"]

        i = 0
        for player in top_3:
            self.assertEqual(player.name, top_players[i])
            i += 1
