from cards import Value
from .player import Player
from .dealer import Dealer


class Rules:
    def __init__(self, player: Player | Dealer):
        self.player = player

        # convert cards to their blackjack values
        self.hand_value_list = [
            self.__blackjack_value(card.value)
            for card in self.player.hand
        ]

    @staticmethod
    def __blackjack_value(card_value: Value) -> int:
        """Returns the blackjack value of a card. Assumes a default value of 11 for aces."""
        val_table = {
            Value.TWO: 2, Value.THREE: 3, Value.FOUR: 4, Value.FIVE: 5,
            Value.SIX: 6, Value.SEVEN: 7, Value.EIGHT: 8, Value.NINE: 9,
            Value.TEN: 10, Value.JACK: 10, Value.QUEEN: 10, Value.KING: 10,
            Value.ACE: 11
        }

        return val_table[card_value]

    def hand_value(self) -> int:
        """evaluates player's hand"""

        # If player busts, replace aces with value = 1
        for idx, val in enumerate(self.hand_value_list):
            is_bust = sum(self.hand_value_list) > 21
            an_ace = 11
            if is_bust and val == an_ace:
                self.hand_value_list[idx] = 1

        return sum(self.hand_value_list)

    def is_blackjack(self) -> bool:
        if self.hand_value() == 21 and len(self.player.hand) == 2:
            return True

    def is_bust(self) -> bool:
        """Determine if the player exceeds a score of 21."""
        return self.hand_value() > 21

    def check_busted(self, player):
        raise NotImplementedError

    # todo can_split
    def can_split(self) -> bool:
        # todo this needs to be finished;
        #  think about how to handle 2 sets at the same time
        if len(self.hand_value_list) > 2:
            return False

        return True
