class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.m_score_player1 = 0
        self.m_score_player2 = 0
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player):
        if player == "player1":
            self.m_score_player1 += 1
        if player == "player2":
            self.m_score_player2 += 1
    
    def get_score(self):
        if self.m_score_player1 == self.m_score_player2: 
            return self.tie_score()
        if self.m_score_player1 >= 4 or self.m_score_player2 >=4:
            return self.advantage_or_winner()
        return self.score()

    def tie_score(self):
        if self.m_score_player1 <= 2:
            return str(self.scores[self.m_score_player1]) + '-All'
        if self.m_score_player1 > 2:
            return "Deuce"
        
    def advantage_or_winner(self):
        score_difference = self.m_score_player1 - self.m_score_player2
        if score_difference == 1:
            return f"Advantage {self.player1}"
        if score_difference == -1:
            return f"Advantage {self.player2}"
        if score_difference >= 2:
             return f"Win for {self.player1}"      
        return f"Win for {self.player2}"     
    
    def score(self):
        player1_score = self.scores[self.m_score_player1]
        player2_score = self.scores[self.m_score_player2]
        return f"{player1_score}-{player2_score}"

 