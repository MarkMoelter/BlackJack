from Player import Player


class PlayerDatabase:
    """Database for all players in the game"""
    def __init__(self, num_players: int = 0):
        self.player_list: list[Player] = [
            Player(input(f"Enter player {num + 1}'s name: "))
            for num in range(num_players)
        ]

    def __repr__(self) -> str:
        out = [f"{repr(player)}\n" for player in self.player_list]
        return ''.join(out)
