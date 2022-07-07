from abc import ABC, abstractmethod
from Cards import Card, CardShoe, Deck


class Shuffle(ABC):

    @abstractmethod
    def shuffle(self, card_list: Deck | CardShoe) -> list[Card]:
        """Shuffle a list"""


class RandomShuffle(Shuffle):
    def shuffle(self, card_list: Deck | CardShoe) -> list[Card]:
        pass


class IndianShuffle(Shuffle):
    def shuffle(self, card_list: Deck | CardShoe) -> list[Card]:
        pass
