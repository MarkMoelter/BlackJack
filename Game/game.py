from player import Player


class Game:
    def __init__(self, num_players=1):
        self.num_players = num_players
        self.players = [
            Player(input(f"Enter player {num + 1}'s name: "))
            for num in range(self.num_players)
        ]

    def show_players(self):
        for player in self.players:
            print(player)
