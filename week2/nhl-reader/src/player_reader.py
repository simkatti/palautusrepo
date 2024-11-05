import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

<<<<<<< HEAD
=======

>>>>>>> edb1e02 (week2 submissions)
    def read(self):
        players = []
        response = requests.get(self.url).json()
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players
