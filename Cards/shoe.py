import random

from .card import Card
from .deck import Deck


class Shoe:
    """Representation of multiple decks of cards."""
    def __init__(self, decks: int = 6):
        # generate shoe from the num of decks
        self.shoe = [card for _ in range(decks) for card in Deck().deck]
        random.shuffle(self.shoe)  # shuffle the shoe

    def __repr__(self):
        output = [f'{card}\n' for card in self.shoe]
        return ''.join(output)

    def deal(self) -> Card:
        """Deal out cards from the shoe"""
        return self.shoe.pop()
