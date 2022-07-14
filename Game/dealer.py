from .player import Player
from Cards import Card


class Dealer(Player):
    def __init__(self, hand: Card | list[Card] = None):
        super().__init__()

        if hand is not None:
            self.hand = hand
