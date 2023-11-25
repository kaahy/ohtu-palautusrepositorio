SCORE_WORDS = ("Love", "Fifteen", "Thirty", "Forty")

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.points = {player1_name: 0, player2_name: 0}

    def won_point(self, player_name):
        self.points[player_name] += 1

    def get_score(self):
        points1 = self.points[self.player1_name]
        points2 = self.points[self.player2_name]

        if points1 == points2:
            return self.tasapeli(points1)
        elif points1 >= 4 or points2 >= 4:
            return self.ylitetty_3(points1, points2)
        else:
            return self.molemmilla_alle_4(points1, points2)

    def tasapeli(self, points):
        if points in (0, 1, 2):
            return SCORE_WORDS[points] + "-All"
        return "Deuce"
    
    def ylitetty_3(self, points1, points2):
        point_difference = points1 - points2
        
        if point_difference == 1:
            return f"Advantage {self.player1_name}"
        elif point_difference == -1:
            return f"Advantage {self.player2_name}"
        elif point_difference >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"
    
    def molemmilla_alle_4(self, points1, points2):
        return SCORE_WORDS[points1] + "-" + SCORE_WORDS[points2]
