import random

from .Suite import Suite
from .Value import Value


class Card:
    def __init__(self, suite: Suite, value: Value):
        self.suite = suite
        self.value = value

    def __repr__(self):
        return f"Card({self.value}, {self.suite})"


def shuffle(card_list: list[Card]) -> None:
    random.shuffle(card_list)
