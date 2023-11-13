class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        all_players = self.reader.get_players()

        players_from_country = []

        for player in all_players:
            if player.nationality == nationality:
                players_from_country.append((player, player.points))

        def jarjestys(x):
            return x[1]
        
        players_from_country = sorted(players_from_country, key=jarjestys, reverse=True)

        top_players_from_country = []

        for player in players_from_country:
            top_players_from_country.append(player[0])

        return top_players_from_country
