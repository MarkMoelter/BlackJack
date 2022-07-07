from enum import Enum, auto

DECKS_IN_SHOE = 6


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


class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in Suite for v in Value]

    def __repr__(self):
        output = [f'{card}\n' for card in self.cards]
        return ''.join(output)

    def shuffle(self):
        """Shuffle the list of cards"""


class CardShoe:
    def __init__(self):
        self.shoe = [card for _ in range(DECKS_IN_SHOE) for card in Deck().cards]

    def __repr__(self):
        output = [f'{card}\n' for card in self.shoe]
        return ''.join(output)


if __name__ == "__main__":
    print(len(CardShoe().shoe))
    print(CardShoe())
