from Cards import Card


class Player:
    """"Store information about a player"""
    def __init__(self, name: str, account_balance: int = 100, cards: tuple[Card] = ()):
        self.name = name
        self.balance = account_balance
        self.cards = cards

    # representations
    def __repr__(self) -> str:
        return f"Person('{self.name}', {self.balance}, {self.cards})"

    def __str__(self) -> str:
        return f'({self.name}, {self.balance}, {self.cards})'

    # betting
    def bet(self, amount: int):
        """Return and subtract the amount from the player's account"""
        if amount > self.balance:
            raise ValueError("Amount must be smaller than player's balance")
        self.balance -= amount

    def check_balance(self) -> int:
        return self.balance

    def set_cards(self, *args: Card):
        self.cards: tuple[Card] = tuple(card for card in args)
