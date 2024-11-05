class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.read()

    def top_scorers_by_nationality(self, nationality):
        players = []
        for player in self.players:
            if player.nationality == nationality:
                players.append(player)
        
        players_by_score = sorted(players, key=lambda player: player.points, reverse=True)
            
            
        return players_by_score[:10]
