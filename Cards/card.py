from enum import Enum, auto


class Suite(Enum):
    DIAMOND = auto()
    CLUB = auto()
    HEART = auto()
    SPADE = auto()


class Value(Enum):
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()


class Card:
    def __init__(self, suite: Suite, value: Value):
        self.suite = suite
        self.value = value

    def __repr__(self):
        return f"Card({self.value}, {self.suite})"
