from cards import Card
from game import funcs


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
        self.bet_amount = 0

        if hand is not None and isinstance(hand, list):
            self.hand = hand

    # representations
    def __repr__(self) -> str:
        return f"Person('{self.name}', {self.balance}, {self.hand})"

    def __str__(self) -> str:
        return f'({self.name}, {self.balance}, {self.hand})'

    def show_hand(self):
        return self.hand

    # betting
    def bet(self, amount: int):
        """Subtract the amount from the player's account"""
        more_than_balance = amount > self.balance
        negative_amount = amount < 0

        if more_than_balance or negative_amount:
            raise ValueError('Invalid amount...')

        self.bet_amount += amount
        self.balance -= amount

    def deposit(self, amount: int):
        """Deposit the given amount into the player's balance."""
        negative_amount = amount < 0
        if negative_amount:
            raise ValueError('Invalid amount...')

        self.balance += amount

    def check_balance(self) -> int:
        return self.balance

    def add_cards(self, cards: list[Card] | Card) -> None:
        """Append card to list if objects are cards"""
        self.hand.append(funcs.validate_obj_list(cards, Card))

    def clear_hand(self):
        self.hand.clear()
