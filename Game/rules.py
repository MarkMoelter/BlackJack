from Cards import Value, Card

ACE_DIFFERENCE = 11 - 1


class Rules:
    def __init__(self, player_hand: list[Card]):
        self.hand = player_hand

    def is_blackjack(self) -> bool:
        if self.hand_value() == 21 and len(self.hand) == 2:
            return True

    def is_bust(self) -> bool:
        """Determine if the player exceeds a score of 21."""
        if self.hand_value() > 21:
            return True

    def hand_value(self) -> int:
        """evaluates player's hand"""

        card_values = [
            self.blackjack_value(card.value)
            for card in self.hand
        ]

        value_sum = sum(card_values)

        # change aces if they bust
        count_aces = card_values.count(11)  # count aces in list

        if count_aces > 0 and value_sum > 21:
            return value_sum - (count_aces * ACE_DIFFERENCE)

        return value_sum

    @staticmethod
    def blackjack_value(card_value: Value) -> int:
        """Returns the blackjack value of a card."""
        val_table = {
            Value.TWO: 2, Value.THREE: 3, Value.FOUR: 4, Value.FIVE: 5,
            Value.SIX: 6, Value.SEVEN: 7, Value.EIGHT: 8, Value.NINE: 9,
            Value.TEN: 10, Value.JACK: 10, Value.QUEEN: 10, Value.KING: 10,
            Value.ACE: 11
        }

        return val_table[card_value]
