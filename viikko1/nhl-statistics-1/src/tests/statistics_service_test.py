import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_nimihaku_palauttaa_pelaajan_tiedot(self):
        tulos = self.stats.search("Semenko")
        self.assertEqual(str(tulos), str(Player("Semenko", "EDM", 4, 12)))

    def test_nimihaku_olemattomalla_nimella_palauttaa_none(self):
        self.assertEqual(self.stats.search("Semenkooo"), None)

    def test_joukkuehaku_antaa_pelaajien_tiedot(self):
        tulos = self.stats.team("EDM")
        oikea = [
            "Semenko EDM 4 + 12 = 16",
            "Kurri EDM 37 + 53 = 90",
            "Gretzky EDM 35 + 89 = 124"
        ]
        self.assertEqual([str(x) for x in tulos], oikea)

    def test_top_antaa_oikeat_pelaajat(self):
        tulos = [str(x) for x in self.stats.top(5)]
        oikea = [
            "Gretzky EDM 35 + 89 = 124",
            "Lemieux PIT 45 + 54 = 99",
            "Yzerman DET 42 + 56 = 98",
            "Kurri EDM 37 + 53 = 90",
            "Semenko EDM 4 + 12 = 16"
        ]
        self.assertEqual(tulos, oikea)

    