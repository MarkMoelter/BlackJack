import unittest
from cards import Card, Deck, Shoe, Value, Suite


class TestCards(unittest.TestCase):
    def setUp(self) -> None:
        card = Card(Suite.CLUB, Value.ACE)

    def test_card(self) -> None:
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
