"""Module responsible for reading the information from the Internet."""

from urllib import request
from player import Player

class PlayerReader:
    """Class for an object reading playres from data."""

    def __init__(self, url):
        self._url = url

    def get_players(self):
        """Method writing and returning a list of players fron the Internet data."""
        players_file = request.urlopen(self._url)
        players = []

        for line in players_file:
            decoded_line = line.decode("utf-8")
            parts = decoded_line.split(";")

            if len(parts) > 3:
                player = Player(
                    parts[0].strip(),
                    parts[1].strip(),
                    int(parts[3].strip()),
                    int(parts[4].strip())
                )

                players.append(player)

        return players
