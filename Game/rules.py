from Cards import Value, Card


class Rules:
    def __init__(self, player_hand: list[Card]):

        self.hand_value_list = [
            self.__blackjack_value(card.value)
            for card in player_hand
        ]

    @staticmethod
    def __blackjack_value(card_value: Value) -> int:
        """Returns the blackjack value of a card."""
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
            bust_with_aces = (val == 11) and sum(self.hand_value_list) > 21
            if bust_with_aces:
                self.hand_value_list[idx] = 1

        return sum(self.hand_value_list)

    def is_blackjack(self) -> bool:
        if self.hand_value() == 21 and len(self.hand_value_list) == 2:
            return True

    def is_bust(self) -> bool:
        """Determine if the player exceeds a score of 21."""
        if self.hand_value() > 21:
            return True
