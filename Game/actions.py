from Cards import Card, Shoe


def hit(shoe: Shoe) -> Card:
    return shoe.deal()
