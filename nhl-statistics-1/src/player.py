"""Module for a player object."""

class Player:
    """Player class for a player object."""
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    @property
    def points(self):
        """Method counting and returning how many points a player has."""
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.points}"
