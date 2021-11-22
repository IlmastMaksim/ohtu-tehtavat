import requests
from player import Player
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )

        players.append(player)

    now = datetime.now()
    print(f"Players from FIN {now}")

    fin_players = list(filter(lambda player: (player.nationality == "FIN"), players))
    sorted_fin_players = reversed(sorted(fin_players, key=lambda player: player.points))
    for player in sorted_fin_players: 
        print(player)

if __name__ == "__main__":
    main()
