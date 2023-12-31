class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.points = self.assists + self.goals ##
    
    def __str__(self):
        return f"{self.name} ({self.team}) - goals: {self.goals} - assists: {self.assists} - points: {self.points}"
