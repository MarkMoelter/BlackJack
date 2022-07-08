import random

from .Card import Card
from .Suite import Suite
from .Value import Value


class Deck:
    """Representation of a deck of cards."""

    def __init__(self):
        self.deck = [Card(s, v) for s in Suite for v in Value]
        random.shuffle(self.deck)

    def __repr__(self):
        output = [f'{card}\n' for card in self.deck]
        return ''.join(output)

    def deal(self) -> Card:
        return self.deck.pop()
