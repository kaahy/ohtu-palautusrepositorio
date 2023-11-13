import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == "FIN":
            players.append((player, player.goals + player.assists))

    def jarjestys(x):
        return x[1]

    players = sorted(players, key=jarjestys, reverse=True)

    print("Players from FIN:\n")

    for player in players:
        print(f"{player[1]} points: {player[0]}")

main()
