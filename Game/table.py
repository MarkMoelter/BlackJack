from player import Player


class Table:
    def __init__(self, player: list[Player] | Player):
        self.players = []

        if isinstance(player, list):
            for obj in player:
                if isinstance(obj, Player):
                    self.players.append(obj)

        if isinstance(player, Player):
            self.players.append(player)
