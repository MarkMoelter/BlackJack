import Game.funcs as funcs
from Cards import Card


class Player:
    """"Store information about a player"""

    def __init__(self,
                 name: str = '',
                 account_balance: int = 100,
                 hand: list[Card] = None
                 ):

        self.name = name
        self.balance = account_balance
        self.hand = []
        self.bet = 0

        if hand is not None and isinstance(hand, list):
            self.hand = hand

    # representations
    def __repr__(self) -> str:
        return f"Person('{self.name}', {self.balance}, {self.hand})"

    def __str__(self) -> str:
        return f'({self.name}, {self.balance}, {self.hand})'

    @property
    def hand(self):
        return self.hand

    # betting
    def bet(self, amount: int):
        """Return and subtract the amount from the player's account"""
        more_than_balance = amount > self.balance
        negative_amount = amount < 0

        if more_than_balance or negative_amount:
            raise ValueError('Invalid amount...')

        self.bet += amount
        self.balance -= amount

    def deposit(self, amount: int):
        negative_amount = amount < 0

        if negative_amount:
            raise ValueError('Invalid amount...')

        self.balance += amount

    def check_balance(self) -> int:
        return self.balance

    @hand.setter
    def hand(self, cards: list[Card] | Card) -> None:
        """Append card to list if objects are cards"""
        self.hand.append(funcs.validate_obj_list(cards, Card))

    def clear_hand(self):
        self.hand.clear()
