class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality= dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.points = self.goals + self.assists

<<<<<<< HEAD
=======

>>>>>>> edb1e02 (week2 submissions)
    def __str__(self):
        return f"{self.name:20} {self.nationality}, team: {self.team}, goals: {self.goals}, assists: {self.assists}, points: {self.points}"
    

