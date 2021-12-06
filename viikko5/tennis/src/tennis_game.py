class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score  = 0
        self.player2_score  = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score  = self.player1_score  + 1
        else:
            self.player2_score  = self.player2_score  + 1
    
    def get_equal_score(self):
        if self.player1_score  == self.player2_score :
            if self.player1_score  == 0:
                return "Love-All"
            elif self.player1_score  == 1:
                return "Fifteen-All"
            elif self.player1_score  == 2:
                return "Thirty-All"
            elif self.player1_score  == 3:
                return "Forty-All"
            else:
                return "Deuce"

    def get_unequal_score(self):
        minus_result = self.player1_score  - self. player2_score 

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
    
    def get_unequal_score_less_3_points(self):
        score = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_score 
            else:
                score = score + "-"
                temp_score = self.player2_score 

            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
                
        return score 

    def get_score(self):

        if self.player1_score  == self.player2_score  and self.player1_score <= 4:
            return self.get_equal_score()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_unequal_score()
        else:
            return self.get_unequal_score_less_3_points()
