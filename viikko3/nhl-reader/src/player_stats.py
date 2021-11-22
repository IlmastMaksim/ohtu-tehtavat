
class PlayerStats:
    def __init__(self, reader) -> None:
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):  
        players = self.reader.get_players()
        players_by_nationality = list(filter(lambda player: (player.nationality == nationality), players))
        sorted_players_by_nationality = reversed(sorted(players_by_nationality, key=lambda player: player.points))

        return sorted_players_by_nationality