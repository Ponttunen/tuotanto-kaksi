"""Module providing a class to handle player data"""

class StatisticsService:
    """Class providing a code to handle player data"""

    def __init__(self, reader):

        self._players = reader.get_players()

    def search(self, name):
        """Method returning player-object name matches?"""
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        """Method returning players of a particular team."""
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many):
        """Method returning a list of players with top scores."""
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(player):
            return player.points

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
