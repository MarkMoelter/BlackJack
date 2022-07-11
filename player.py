from Cards import Card


class Player:
    """"Store information about a player"""
    def __init__(self, name: str, account_balance: int = 100):
        self.name = name
        self.balance = account_balance
        self.cards = []

    # representations
    def __repr__(self) -> str:
        return f"Person('{self.name}', {self.balance}, {self.cards})"

    def __str__(self) -> str:
        return f'({self.name}, {self.balance}, {self.cards})'

    # betting
    def bet(self, amount: int):
        """Return and subtract the amount from the player's account"""
        if amount > self.balance:
            raise ValueError('Amount greater than current balance...')
        self.balance -= amount

    def check_balance(self) -> int:
        return self.balance

    def set_cards(self, *args: Card):
        """Append card to list if objects are cards"""
        for arg in args:
            if not isinstance(arg, Card):
                raise TypeError('Invalid object type...')

            self.cards.append(arg)
