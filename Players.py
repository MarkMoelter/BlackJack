from Cards import Card, Value, Suite


class Player:
    """"Store information about each player"""

    def __init__(self, name: str, account_balance: int = 100, cards: tuple[Card] = ()):
        self.name = name
        self.balance = account_balance
        self.cards = cards

    def __repr__(self) -> str:
        return f"Person('{self.name}', {self.balance}, {self.cards})"

    def __str__(self) -> str:
        return f'({self.name}, {self.balance}, {self.cards})'

    def bet(self, amount: int):
        """Return and subtract the amount from the player's account"""
        if amount > self.balance:
            raise ValueError("Amount must be smaller than player's balance")
        self.balance -= amount

    def check_balance(self) -> int:
        return self.balance

    def set_cards(self, *card: Card):
        self.cards: tuple[Card] = tuple(card for card in card)


if __name__ == "__main__":
    player = Player('Mark', 1000)
    card = Card(suite=Suite.CLUB, value=Value.ACE)
    player.set_cards(card)
